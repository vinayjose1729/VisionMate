from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')


def adminhome(request):
    return render(request,'adminpanel/adminpanel.html')

def caretaker(request):
    return render(request,'adminpanel/verify.html')

def admin_view_blind_users(request):
    return render(request,'adminpanel/admin_view_blind_users.html')


def admin_view_complaint(request):
    return render(request,'adminpanel/admin_view_complaint.html')

def admin_view_feedback(request):
    return render(request,'adminpanel/admin_view_feedback.html')

def admin_complaint_reply(request):
    return render(request,'adminpanel/admin_complaint_reply.html')





