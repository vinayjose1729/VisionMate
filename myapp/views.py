from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from myapp.models import *


# Create your views here.


def home(request):
    return render(request,'home.html')


@csrf_exempt
@never_cache
def login(request):
    if request.method == "POST":
        uname = request.POST['username']
        password = request.POST['password']
        # a = User.objects.get(username=uname).first()
        # if a:
        #     if uname == a.username:

        user = authenticate(request, username=uname, password=password)
        print("USER : ", user)

        if user is not None:
            auth_login(request, user)
            request.session['user_id'] = user.id  # Auth user ID

            if user.groups.filter(name='admin').exists():
                return redirect('adminpanel')

            else:
                messages.error(request, 'Group not exists')
                return redirect('login')
        # else:
        #     messages.error(request, 'Username or password incorrect')
        #     else:
        #         messages.error(request, 'Invalid username')
        #         return redirect('login')

        else:
            messages.error(request, 'No such user exist in this platform')
            return redirect('login')
    return render(request, 'home.html')


def adminpanel(request):
    return render(request,'adminpanel/adminpanel.html')

from django.shortcuts import render
from .models import Caretaker

def admin_manage_caretakers(request):
    caretakers = Caretaker.objects.all()
    return render(request, 'adminpanel/view_caretakers.html', {'caretakers': caretakers})

def approve_caretakers(request,id):
    print("id : ",id)
    cc = Caretaker.objects.get(id=id)
    cc.approval_status="Approved"
    cc.save()
    return redirect('view_caretakers')

def reject_caretakers(request,id):
   print("id: ",id)
   cc = Caretaker.objects.get(id=id)
   cc.approval_status="Rejected"
   cc.save()
   return redirect('view_caretakers')

def admin_view_blind_users(request):
    return render(request,'adminpanel/admin_view_blind_users.html')


def admin_view_complaint(request):
    return render(request,'adminpanel/admin_view_complaint.html')

def admin_view_feedback(request):
    return render(request,'adminpanel/admin_view_feedback.html')

def admin_complaint_reply(request):
    return render(request,'adminpanel/admin_complaint_reply.html')


def caretaker_register(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            gender = request.POST['gender']
            place = request.POST['place']
            phone = request.POST['phone']
            photo = request.FILES['photo']
            proof = request.FILES['idproof']
            username = request.POST['username']
            password = request.POST['password']

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')

            # Create user using Django's auth system
            user= User.objects.create_user(username=username, password=password)
            user.save()

            try:
                group = Group.objects.get(name='caretaker')
            except Group.DosNotExist:
                group = Group.objects.create(name='caretaker')
            user.groups.add(group)

            # Create care center profile
            Caretaker.objects.create(
                user=user,
                name=name,
                email=email,
                gender=gender,
                place=place,
                phone=phone,
                id_proof=proof,
                photo=photo,
                approval_status='pending',
            )

            return JsonResponse({'status': 'success', 'message': 'Registration successful'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def user_login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        auth_login(request, user)

        # Get first group name
        group_name = user.groups.values_list('name', flat=True).first()

        # Default approval_status
        approval_status = None

        # Check based on group and fetch approval_status
        if group_name == 'caretaker':
            try:
                approval_status = Caretaker.objects.get(user=user).approval_status
            except Caretaker.DoesNotExist:
                approval_status = None

        elif group_name == 'users':
            try:
                approval_status = Blind_User.objects.get(user=user)
            except Blind_User.DoesNotExist:
                approval_status = None

        return JsonResponse({
            'status': 'success',
            'lid': str(user.id),
            'group_name': group_name,
            'approval_status': approval_status
        })

    else:
        return JsonResponse({'status': 'error'})


@csrf_exempt
def user_view_profile(request):
    lid = request.POST['lid']

    a = user_login.objects.get(USER_id=lid)

    data = {
        "name": a.name,
        "email": a.email,
        "phone": a.phone,
        "place": a.place,
        "id": a.id,
        # add other fields you have in your model
    }

    return JsonResponse({'status': 'success', 'data': data})

@csrf_exempt
def user_edit_profile(request):
    lid = request.POST['lid']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    place = request.POST['place']


    # Get the user profile
    a = Caretaker.objects.get(USER_id=lid)

    # Update the profile fields
    a.name = name
    a.email = email
    a.phone = phone
    a.place = place


    a.save()

    return JsonResponse({'status': 'success', 'message': 'Profile updated successfully'})



