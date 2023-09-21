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
    path('register/', views.user_register, name='register'), # 求职者
    path('login/', views.user_login, name='login'),
    path('eregister/', views.e_register, name='eregister'), # 招聘者
    path('elogin/', views.e_login, name='elogin'),
    path('logout/', views.user_logout, name='logout'), # 退出
    path('', views.home, name="home"), # 主页
    path('ehome/',views.e_home,name="ehome"),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'), # 工作详情
    path('search/', views.job_search, name='job_search'), # 主页搜索框
    path('profile/', views.profile, name='profile'),  # 个人中心页面
    path('w_resume/', views.w_resume, name='w_resume'),  # 填写简历页面
    path('edit_resume/<int:resume_id>/', views.edit_resume, name='edit_resume'),  # 编辑简历页面
    path('apply_job/<int:job_id>/', views.apply_job, name='apply_job'),
    path('eprofile/',views.e_profile,name='eprofile'),
    path('view_applications/', views.view_applications, name='view_applications'),
    path('create_job/', views.create_job, name='create_job'),
    path('edit_job/<int:job_id>/', views.edit_job, name='edit_job'),
    path('eview_applications/', views.eview_applications, name='eview_applications'),
    path('eview_resume/<int:resume_id>/', views.eview_resume, name='eview_resume'),
]
