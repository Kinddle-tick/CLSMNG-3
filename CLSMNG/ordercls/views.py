from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import OrderForm
from django.http import HttpResponseRedirect, Http404
from .models import FeedBack
# Create your views here.

def default(request):
    return render(request, 'error.html')

# def cls(request):
#     return render(request, '主页-教室.html')

def inquiry(request):
    return render(request, 'inquiry.html')

def feedback(request):
    select_reason_list=["实际用途与申请不符","实际使用时间与申请不符","桌椅损坏","多媒体设备故障","其他"]
    context = {'form': None, "reason_list":select_reason_list, "hint":''}
    if request.POST:
        print(request.POST)
        print(request.POST.get('feedback-select-reason'))
        # new_recode = FeedBack()
        # new_recode.reason = request.POST.get('feedback-select-reason')
        FeedBack.objects.create(reason=request.POST.get('feedback-select-reason'),
                                text=request.POST.get('feedback-message'))
        context['hint'] = '😄提交成功！请耐心等待工作人员的处理'
    return render(request, 'feedback.html', context)


    # """modelsform版本"""
    # if request.method != 'POST':
    #     form = FeedBackForm()
    # else:
    #     form = FeedBackForm(request.POST)
    #     form.save()
    #     return redirect(request)
    # context = {'form': form}
    # return render(request, 'feedback.html', context)

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