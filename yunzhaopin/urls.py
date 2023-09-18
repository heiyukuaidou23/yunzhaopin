"""
URL configuration for yunzhaopin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from app1 import views
# from app1.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('eregister/', views.e_register, name='eregister'),
    path('elogin/', views.e_login, name='elogin'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name="home"),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('search/', views.job_search, name='job_search'),
    # path('jobs/', views.job_list, name='job_list'),  # 职位列表URL
    path('profile/', views.profile, name='profile'),  # 个人中心页面
    path('w_resume/', views.w_resume, name='w_resume'),  # 编辑简历页面
]
