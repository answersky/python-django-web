from django.shortcuts import HttpResponseRedirect

# 自定义拦截器
try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class SimpleMiddleware(MiddlewareMixin):
  def process_request(self, request):
    print("请求链接："+request.path)
    pass