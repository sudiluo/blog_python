from django.shortcuts import render


def data(request):
    string = "字符串测试显示"
    mylist = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'web/data.html', {'s': string} ,{'mylist' : mylist})