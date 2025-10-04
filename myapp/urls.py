from django.urls import path

from myapp import views

urlpatterns = [
    path('',views.home,name ='home'),
    path('login',views.login,name ='login'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('caretaker', views.caretaker, name='caretaker')

]