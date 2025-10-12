from django.urls import path

from myapp import views

urlpatterns = [
    path('',views.home,name ='home'),
    path('login',views.login,name ='login'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('caretaker', views.caretaker, name='caretaker'),
    path('admin_view_blind_users',views.admin_view_blind_users,name='admin_view_blind_users'),
    path('admin_view_complaint',views.admin_view_complaint,name='admin_view_complaint'),
    path('admin_view_feedback', views.admin_view_feedback, name='admin_view_feedback'),
    path('admin_complaint_reply', views.admin_complaint_reply, name='admin_complaint_reply')

]