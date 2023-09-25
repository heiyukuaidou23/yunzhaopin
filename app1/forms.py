from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import JobSeeker, Employer, Resume, Job


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = JobSeeker
        fields = ['username', 'password']


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = JobSeeker
        fields = ['username', 'password']


class ELoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Employer
        fields = ['username', 'password']


class ERegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    error_messages = {
        'name': {'required': '此项是必填的'}  # 设置错误提示信息
    }

    class Meta:
        model = Employer
        fields = ['username', 'password']


class JobFilterForm(forms.Form):
    category = forms.CharField(max_length=100, required=False)  # 添加职位类别字段
    keyword = forms.CharField(max_length=100, required=False, widget=forms.HiddenInput)  # 添加关键字字段
    # 添加其他筛选条件字段


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        # fields = '__all__'
        exclude = ['user']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '姓名'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '年龄'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '联系方式'}),
            'job_status': forms.Select(attrs={'class': 'form-control'}),
            'job_expectation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '求职期望'}),
            'work_experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '工作/实习经历'}),
            'project_experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '项目经历'}),
            'education': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '教育程度'}),
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '专业技能'}),
        }

# 在这里可以添加自定义的表单字段或验证逻辑，根据实际需要

class ApplyJobForm(forms.Form):
    pass  # 这里可以添加表单字段，如果需要的话


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        # fields = '__all__'
        exclude = ['employer']

    # 添加自定义的样式和布局
    widgets = {
        'companyName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '公司名称'}),
        'companySize': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '公司人数'}),
        'education': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '教育程度'}),
        'workName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '工作名称'}),
        'salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '薪资待遇'}),
        'workCity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '工作城市'}),
        'workingExp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '经验要求'}),
    }
