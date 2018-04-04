from django.http import HttpResponse
from django.shortcuts import render

from web import mysqlDB
from web.models import models

# request参数必须有，封装用户所有请求内容
def index(request):
    mysqlDB.testconnect()
    # 不能直接返回字符串，django的规范必须用HttpResponse封装。
    return render(request, 'web/home.html')


def test(request):
    orderModel = models.OrderModel.objects.get(order_num='123456789')
    print(orderModel.user_id)
    return HttpResponse(orderModel.__dict__.items())

def findOrder(request):
    orderModel = models.OrderModel.objects.get(order_num='123456789')
    print(orderModel.user_id)
    return HttpResponse(orderModel.__dict__.items())

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