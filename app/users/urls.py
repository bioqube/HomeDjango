from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
        path('login/', auth, name='login'),
        path('registration/', registration, name='registration'),
        path('profile/', profile, name='profile'),
        path('logout', logout, name='logout'),
    ]