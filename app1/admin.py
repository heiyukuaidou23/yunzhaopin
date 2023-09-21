from django.contrib import admin
from app1.models import JobSeeker, Job, Employer, Resume

admin.site.site_header = '云招聘管理后台'  # 设置header
admin.site.site_title = '云招聘管理后台'   # 设置title
admin.site.index_title = '云招聘管理后台'



class Users(admin.ModelAdmin):
    list_display = ['username']
admin.site.register(JobSeeker,Users)

class Hr(admin.ModelAdmin):
    list_display = ['username','last_login']

admin.site.register(Employer,Hr)
class Job_list(admin.ModelAdmin):
    list_display = ['companyName','companySize','education','workName','salary']

admin.site.register(Job,Job_list)

class Resume_list(admin.ModelAdmin):
    list_display = ['name','age','gender','contact','skills']

admin.site.register(Resume,Resume_list)

