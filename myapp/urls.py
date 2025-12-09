from django.urls import path

from myapp import views

urlpatterns = [
    path('',views.home,name ='home'),
    path('login',views.login,name ='login'),
    path('adminpanel', views.adminpanel, name='adminpanel'),



    path('view_caretakers/', views.admin_manage_caretakers, name='view_caretakers'),
    path('approve_caretakers/<id>', views.approve_caretakers, name='approve_caretakers'),
     path('reject_caretakers/<id>', views.reject_caretakers, name='reject_caretakers'),




    path('admin_view_blind_users',views.admin_view_blind_users,name='admin_view_blind_users'),
    path('admin_view_complaint',views.admin_view_complaint,name='admin_view_complaint'),
    path('admin_view_feedback', views.admin_view_feedback, name='admin_view_feedback'),
    path('admin_complaint_reply', views.admin_complaint_reply, name='admin_complaint_reply'),




    path('caretaker_register/', views.caretaker_register, name='caretaker_register'),

    path('user_login/', views.user_login, name='user_login'),

    path('user_view_profile/', views.user_view_profile, name='user_view_profile'),
    path('user_edit_profile/', views.user_edit_profile, name='user_edit_profile'),

]