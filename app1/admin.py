from django.contrib import admin
from app1.models import JobSeeker, Job, Employer, Resume

admin.site.site_header = '云招聘管理后台'  # 设置header
admin.site.site_title = '云招聘管理后台'  # 设置title
admin.site.index_title = '云招聘管理后台'


class Users(admin.ModelAdmin):
    list_display = ['username']


admin.site.register(JobSeeker, Users)


class Hr(admin.ModelAdmin):
    list_display = ['username', 'last_login']


admin.site.register(Employer, Hr)


class Job_list(admin.ModelAdmin):
    ordering = ['-id']
    list_filter = ['workName']
    list_display = ['companyName', 'companySize', 'education', 'workName', 'salary']
    list_per_page = 10
    # list_max_show_all = 200
    # 使用 get_readonly_fields 方法来返回所有字段的只读版本
    def get_readonly_fields(self, request, obj=None):
        if obj:
            # 如果是编辑已有对象，则返回所有字段的只读版本
            return [field.name for field in obj._meta.fields]
        # 如果是创建新对象，则返回空列表
        return []


admin.site.register(Job, Job_list)


class Resume_list(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender', 'contact', 'skills']
    # fields = ['name','age','gender', 'contact', 'skills','job_status','job_expectation','work_experience']
    exclude = ['user']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            # 如果是编辑已有对象，则返回所有字段的只读版本
            return [field.name for field in obj._meta.fields]
        # 如果是创建新对象，则返回空列表
        return []


admin.site.register(Resume, Resume_list)
