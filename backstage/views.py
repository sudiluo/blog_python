from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response
from users.models import User

# request参数必须有，封装用户所有请求内容
def index(request):
    # 不能直接返回字符串，django的规范必须用HttpResponse封装。
    return render(request, 'backstage/index.html')


def testTry():
    try:
        fh = open("testfile", "w")
        try:
            fh.write("This is my test file for exception handling!!")
        finally:
            print("Going to close the file")
            fh.close()
    except IOError:
        print("Error: can\'t find file or read data")


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a + b))


def loginUser(request):
    return render(request, 'backstage/login.html')


def userList(request):
    data = User.objects.values()
    list = User.objects.all()
    return render(request, 'backstage/userlist.html', context={'user_list': list})