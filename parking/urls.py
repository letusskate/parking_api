"""parking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from apps.users.views import get_userinfo, RegisterView, ChangePasswordView, UserLoginView, GetMoneyView, AddMoneyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userinfo', csrf_exempt(get_userinfo)),
    path('api/users/register', csrf_exempt(RegisterView.as_view())),
    path('api/users/login',csrf_exempt(UserLoginView.as_view())),
    path('api/users/change-password', csrf_exempt(ChangePasswordView.as_view())),
    path('api/users/get-money', csrf_exempt(GetMoneyView.as_view())),
    path('api/users/add-money', csrf_exempt(AddMoneyView.as_view())),
]
