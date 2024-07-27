from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fregister', views.fregister, name='fregister'),
    path('register', views.register, name='register'),
    path('tregister', views.tregister, name='tregister'),
    path('sregister', views.sregister, name='sregister'),
    path('ulogin', views.ulogin, name='ulogin'),
    path('ulogout', views.ulogout, name='ulogout'),
    path('adminpage', views.adminpage, name='adminpage'),
    path('teacherpage', views.teacherpage, name='teacherpage'),
    path('studentpage', views.studentpage, name='studentpage'),
]