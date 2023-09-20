from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models.expressions import Random
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F, Value
# from django.db.models.functions import Random
from . import models
from .forms import RegistrationForm, LoginForm, ERegistrationForm, ELoginForm, JobFilterForm, ResumeForm, ApplyJobForm
from .models import Job, Resume, Application, JobSeeker


# from .models import Farmer, FamilyMember, IncomeExpense, AssetLiability, BusinessInfo, LoanCredit


# 注册
def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


# 登录
def user_login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {'form': form})
    form = LoginForm(data=request.POST)
    if not form.is_valid():
        return render(request, "login.html", {'form': form})
    user = form.cleaned_data['username']
    pwd = form.cleaned_data['password']
    user_object = models.JobSeeker.objects.filter(username=user, password=pwd).first()
    if not user_object:
        return render(request, "login.html", {'form': form, 'error': "用户名或密码错误"})
    request.session['info'] = {"id": user_object.id, 'name': user_object.username}
    # 设置一个时间为一周
    request.session.set_expiry(60 * 60 * 24 * 7)
    return redirect('home')


# hr注册
def e_register(request):
    if request.method == 'POST':
        form = ERegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('elogin')
    else:
        form = ERegistrationForm()
    return render(request, 'eregister.html', {'form': form})


# hr登录
def e_login(request):
    if request.method == "GET":
        form = ELoginForm()
        return render(request, "elogin.html", {'form': form})
    form = ELoginForm(data=request.POST)
    if not form.is_valid():
        return render(request, "elogin.html", {'form': form})
    user = form.cleaned_data['username']
    pwd = form.cleaned_data['password']
    user_object = models.Employer.objects.filter(username=user, password=pwd).first()
    if not user_object:
        return render(request, "elogin.html", {'form': form, 'error': "用户名或密码错误"})
    request.session['info'] = {"id": user_object.id, 'name': user_object.username}
    # 设置一个时间为一周
    request.session.set_expiry(60 * 60 * 24 * 7)
    return redirect('home')


# 退出
def user_logout(request):
    logout(request)
    return redirect('home')  # 注销成功后重定向到主页面


# @login_required
# 主页
def home(request):
    jobs = Job.objects.all()  # 获取所有职位数据
    paginator = Paginator(jobs, 5)  # 每页显示5个职位
    page_number = request.GET.get('page')  # 获取当前页数，默认为第1页
    jobs = paginator.get_page(page_number)  # 获取当前页的职位数据
    # 获取当前用户信息
    if 'info' in request.session:
        # 用户已登录，隐藏登录与注册按钮
        show_login_register = False
    else:
        # 用户未登录，显示登录与注册按钮
        show_login_register = True
    return render(request, 'home.html', {'jobs': jobs, 'show_login_register': show_login_register})


# 职位详情
# def job_detail(request, job_id):
#     job = get_object_or_404(Job, pk=job_id)
#     return render(request, 'job_detail.html', {'job': job})

# 工作详情
def job_detail(request, job_id):
    # 获取主要职位的信息
    job = Job.objects.get(pk=job_id)

    # 获取所有职位并随机排序
    all_jobs = Job.objects.exclude(pk=job_id)  # 排除当前职位
    related_jobs = all_jobs.annotate(random_order=Random()).order_by('random_order')[:3]  # 随机排序并选择前3个

    # 将相关职位数据传递给模板
    context = {
        'job': job,
        'related_jobs': related_jobs,
    }

    return render(request, 'job_detail.html', context)


# 搜索职位
def job_search(request):
    query = request.GET.get('q', '')  # 获取搜索关键词，默认为空
    page_number = request.GET.get('page')  # 获取当前页数，默认为第一页
    # 查询匹配的职位数据
    results = Job.objects.filter(workName__icontains=query)
    # 分页逻辑
    paginator = Paginator(results, 5)  # 每页显示10条数据
    # 获取当前页的数据
    page = paginator.get_page(page_number)
    return render(request, 'search_result.html', {'page': page, 'query': query})


# def job_list(request):
#     jobs = Job.objects.all()  # 获取所有职位
#
#     # 处理筛选请求
#     if request.method == 'GET':
#         filter_form = JobFilterForm(request.GET)
#         if filter_form.is_valid():
#             category = filter_form.cleaned_data.get('category')
#             keyword = filter_form.cleaned_data.get('keyword')  # 获取关键字
#             if category:
#                 jobs = jobs.filter(workName=category)  # 使用正确的字段名
#             if keyword:
#                 jobs = jobs.filter(workName__icontains=keyword)  # 使用正确的字段名
#
#     return render(request, 'home.html', {'jobs': jobs, 'filter_form': filter_form})

# 个人中心
def profile(request):
    user_info = request.session.get('info')

    if user_info is not None:
        try:
            user_id = user_info['id']
            user = models.JobSeeker.objects.get(id=user_id)
            # 检查是否有关联的简历
            try:
                resumes = Resume.objects.get(user=user)
                return render(request, 'profile.html', {'resumes': resumes})
            except ObjectDoesNotExist:
                # 如果没有简历，重定向到创建简历的页面
                return redirect('w_resume')
        except models.JobSeeker.DoesNotExist:
            return render(request, 'profile.html', {'user_not_found': True})
    else:
        return render(request, 'profile.html', {'user_not_logged_in': True})


# 填写简历
def w_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            # 保存或更新简历数据
            resume = form.save(commit=False)
            resume.save()
            return redirect('profile')  # 重定向到个人中心页面或其他适当的页面
    else:
        form = ResumeForm()

    return render(request, 'w_resume.html', {'form': form})


# 编辑简历
def edit_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)

    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ResumeForm(instance=resume)

    return render(request, 'edit_resume.html', {'form': form, 'resume': resume})


# 简历投递
def apply_job(request, job_id):
    if request.method == 'POST':
        # 获取当前用户的默认简历
        user_info = request.session.get('info')
        if user_info is not None:
            user_id = user_info['id']
            user = get_object_or_404(JobSeeker, id=user_id)
            default_resume = user.resume  # 假设你在 JobSeeker 模型中有一个名为 resume 的 OneToOneField
        else:
            return redirect('login')  # 如果用户未登录，重定向到登录页面

        # 获取职位
        job = get_object_or_404(Job, pk=job_id)

        # 创建申请表单并验证
        form = ApplyJobForm(request.POST)
        if form.is_valid():
            # 创建申请记录并分配默认简历
            application = Application(user=user, job=job, resume=default_resume)
            application.save()
            return redirect('home')  # 重定向到个人中心页面或其他适当的页面
    else:
        # 处理GET请求，显示职位详情页面
        job = get_object_or_404(Job, pk=job_id)
        form = ApplyJobForm()  # 创建申请表单实例

    return render(request, 'job_detail.html', {'job': job, 'form': form})


# 查看投递记录的视图
def view_applications(request):
    user_info = request.session.get('info')
    user_id = user_info['id']
    user = models.JobSeeker.objects.get(id=user_id)
    applications = Application.objects.filter(user=user)
    return render(request, 'applications.html', {'applications': applications})
