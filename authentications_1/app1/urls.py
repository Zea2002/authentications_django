from django.urls import path
from .views import signup_view, login_view, logout_view, profile_view, change_password,home_view

urlpatterns = [
     path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('change-password/', change_password, name='change_password'),
]
