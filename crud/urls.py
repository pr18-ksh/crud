from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('home/',home, name='home'),
    path('add-std/',std_add, name='std_add'),
    path('delete-std/<int:roll>',delete_std ,name='delete_std'),
    path('update-std/<int:roll>',update_std ,name='update_std'),
    path('do-update-std/<int:roll>',do_update_std ,name='do_update_std'),
    path('index/',index,name="index"),
    path('login/',login_page,name="login"),
    path('register/',register_page,name="register"),
    path('logout/',logout_page,name="logout"),
]