from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class JobSeeker(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(verbose_name='Last Login', blank=True, null=True)


class Employer(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(verbose_name='Last Login', blank=True, null=True)


class Job(models.Model):
    companyName = models.CharField(max_length=100, verbose_name='公司名称')  # 公司名称
    companySize = models.CharField(max_length=50, null=True, blank=True, verbose_name='公司人数')  # 公司人数
    education = models.CharField(max_length=20, verbose_name='教育程度')  # 教育程度
    workName = models.CharField(max_length=100, verbose_name='工作名称')  # 工作名称
    # publishTime = models.DateField(null=True, blank=True)              # 上传时间
    salary = models.CharField(max_length=50, verbose_name='薪资待遇')  # 薪资待遇
    workCity = models.CharField(max_length=50, verbose_name='工作城市')  # 工作城市
    workingExp = models.CharField(max_length=50, verbose_name='经验要求')  # 经验要求
    businessType = models.CharField(max_length=255, default='', verbose_name='职位描述')
    # employer = models.ForeignKey(Employer, on_delete=models.CASCADE, default=1)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True)


class Resume(models.Model):
    # 关联到用户
    user = models.OneToOneField(JobSeeker, on_delete=models.CASCADE, related_name='resume')
    # 姓名
    name = models.CharField(max_length=100, verbose_name="姓名")
    # 年龄
    age = models.PositiveIntegerField(verbose_name="年龄")
    # 性别
    GENDER_CHOICES = [
        ('男', '男'),
        ('女', '女'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="性别")
    # 联系方式
    contact = models.CharField(max_length=20, verbose_name="联系方式")
    # 求职状态
    JOB_STATUS_CHOICES = [
        ('积极找工作', '积极找工作'),
        ('暂不找工作', '暂不找工作'),
    ]
    job_status = models.CharField(max_length=20, choices=JOB_STATUS_CHOICES, verbose_name="求职状态")
    # 求职期望
    job_expectation = models.TextField(verbose_name="求职期望")
    # 工作/实习经历
    work_experience = models.TextField(verbose_name="工作/实习经历")
    # 项目经历
    project_experience = models.TextField(verbose_name="项目经历")
    # 教育程度
    education = models.CharField(max_length=100, verbose_name="教育程度")
    # 专业技能
    skills = models.TextField(verbose_name="专业技能")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "个人简历"
        verbose_name_plural = "个人简历"


class Application(models.Model):
    user = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.job.workName}"
