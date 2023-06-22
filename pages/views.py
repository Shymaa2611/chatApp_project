from django.shortcuts import render


def index(request):
    return render(request,'pages/index.html')
def index3(request):
    return render(request,'pages/index3.html')