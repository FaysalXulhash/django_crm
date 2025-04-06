from django.urls import path
from .views import SignUp
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('new', SignUp, name='new-user'),
    path('login/', LoginView.as_view(template_name="userprofile/login.html"), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
]