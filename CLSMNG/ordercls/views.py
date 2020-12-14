from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import TopicForm, EntryForm, FeedBackForm, OrderForm
from django.http import HttpResponseRedirect, Http404

# Create your views here.

def default(request):
    return render(request, 'error.html')

# def cls(request):
#     return render(request, '主页-教室.html')

def inquiry(request):
    return render(request, 'inquiry.html')

def feedback(request):
    """modelsform版本"""
    if request.method != 'POST':
        form = FeedBackForm()
    else:
        form = FeedBackForm(request.POST)
        form.save()
        return redirect(request)
    context = {'form': form}
    return render(request, 'feedback.html', context)

def order(request):
    if request.method != 'POST':
        form = OrderForm()
    else:
        form = OrderForm(request.POST)
        form.save()
        return redirect(request)
    context = {'form': form}
    return render(request, 'order.html', context)

#<!--{#        room.name：教室号；room.num1/room.num2：实际使用人数/可用人数#}-->
def my_request(request):
    return render(request, 'my_request.html')