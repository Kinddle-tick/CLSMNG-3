from django.shortcuts import render

# Create your views here.

def default(request):
    return render(request, 'error.html')

def cls(request):
    return render(request, '主页-教室.html')