# from django.shortcuts import redirect
#
#
# def login_required(view_func):
#     def _wrapped_view(request, *args, **kwargs):
#         if 'info' in request.session:
#             return view_func(request, *args, **kwargs)
#         else:
#             return redirect('login')  # 将用户重定向到登录页面
#
#     return _wrapped_view
