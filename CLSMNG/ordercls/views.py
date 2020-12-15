from django.shortcuts import render, redirect
from django.urls import reverse
# from .forms import OrderForm
from django.http import HttpResponseRedirect, Http404
from .models import FeedBack, ClassroomApply, ClassroomStatus
import datetime
from django.forms.models import model_to_dict
# Create your views here.

def check(classroomID, period, date):
    get = ClassroomStatus.objects.filter(classroomID=classroomID, timePeriod=period, date=date)
    getdic=get.values().first()
    if getdic == None:
        return '未找到该时段的教室'
    return getdic['status']


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
        FeedBack.objects.create(reason=request.POST.get('feedback-select-reason'),
                                text=request.POST.get('feedback-message'))
        context['hint'] = '😄提交成功！请耐心等待工作人员的处理'
    return render(request, 'feedback.html', context)

def order(request):
    context = {"hint": '', "classroom_dic": ["品学楼A", "品学楼B", "品学楼C","立人楼A","立人楼B"],
               "apply_time": [i[1] for i in ClassroomApply.CHOICES_TIMEPIERED],
               "apply_reason":["班级自习", "班级活动", "部门活动", "老师调课", "其他"]}
    if request.POST:
        # print(request.POST)
        classroomID = request.POST.get("select_build")+request.POST.get("local")
        period = request.POST.get("period")
        date = datetime.datetime.now().date()
        status = check(classroomID,period,date)
        user = request.POST.get("user")
        detail = request.POST.get('order-detail')
        if request.POST.get("submit_btn")=='submit':
            if status == "空闲" or status == "可拼":
                reasondic = {'apply_reason':detail, "deny_reason":''}
                ClassroomApply.objects.create(date=date, classroomID=classroomID,
                                              timePeriod=period, userID=user, reason=reasondic)
                context['hint'] = "提交成功， 耐心等待审核哦～"
            else:
                context['hint'] = "提交失败...教室状态："+status
        elif request.POST.get("submit_btn")=='check':
            if status == "空闲" or status == "可拼":
                context['hint'] = "教室状态："+status
            else:
                context['hint'] = "教室状态："+status
        else:
            context['hint'] = "提交失败"

    return render(request, 'order.html', context=context)

#<!--{#        room.name：教室号；room.num1/room.num2：实际使用人数/可用人数#}-->
def my_request(request):
    return render(request, 'my_request.html')

def init(request):
    build = ["品学楼A", "品学楼B", "品学楼C","立人楼A","立人楼B"]
    date = datetime.datetime.now().date()
    classroomID = [i+str(j) for i in build for j in range(101,106)]
    period = [i[1] for i in ClassroomApply.CHOICES_TIMEPIERED]
    initdata = [{"date":date, "classroomID":i, "timePeriod":j}
                for i in classroomID for j in period]
    # 先删除所有内容
    ClassroomStatus.objects.all().delete()
    for i in initdata:
        ClassroomStatus.objects.create(date=i['date'],classroomID=i['classroomID'],
                                       timePeriod=i['timePeriod'])
    print("初始化完成")
    return redirect(reverse("index"))