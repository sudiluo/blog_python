from django.contrib import auth
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.urls import reverse

from .forms import RegisterForm


def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、确认密码、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()
            return render(request, 'users/signin.html', context={'msg': '注册成功'})
        else:
            return render(request, 'users/signup.html', context={'form': form, 'next': redirect_to,'error_messages':form._errors})
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    # 将记录用户注册前页面的 redirect_to 传给模板，以维持 next 参数在整个注册流程中的传递
    return render(request, 'users/signup.html', context={'form': form, 'next': redirect_to})


def index(request):
    return render(request, 'index.html')

def loginIndex(request):
    return render(request, 'users/signin.html')

def loginUser(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    login_form = RegisterForm(request.POST)
    if login_form.is_valid:
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # 如果登入成功，重定向要主页
            return HttpResponseRedirect(reverse('backstage:index'))
        else:
            # user为None，说明账号或密码错误
            return render(request, "users/signin.html", {"msg": "用户名或密码错误"})
    else:
        # 表单无效，返回login_form对象即可，在template调用login_form.errors这个字典去获取相关的错误
        return render(request, "users/signin.html", {"login_form": login_form})
