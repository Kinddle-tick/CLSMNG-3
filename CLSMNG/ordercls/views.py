from django.shortcuts import render, redirect
from django.urls import reverse
# from .forms import OrderForm
from django.http import HttpResponseRedirect, Http404
from .models import FeedBack, ClassroomApply, ClassroomStatus
import datetime, re
from django.utils import timezone
from django.forms.models import model_to_dict
# Create your views here.

#  从数据库中尝试查找该教室是否存在（order的子函数）
def check(classroomID, period, date):
    get = ClassroomStatus.objects.filter(classroomID=classroomID, timePeriod=period, date=date)
    getdic=get.values().first()
    if getdic == None:
        return '未找到该时段的教室'
    return getdic['status']

#  通过过滤数据库的内容按照要求POST的过滤要求展示内容，（inquiry子函数）
def filter(build, field, floor, status, obj):
    print(obj)
    args = [build, field, floor, status]
    checklist=[True if i =="不限" else False for i in args]
    mapfloor = {'一层': "1", "二层": "2", "三层": "3", "四层": "4", "五层": "5"}
    room = obj.classroomID
    Thebuild = re.match(".*[^0-9A-Za-z]", room).group()
    Thefield = re.search('[A-Za-z]',room)[0]
    Thefloor = re.search("[0-9]",room)[0]
    Thestatus= obj.status

    if Thebuild == build:
        checklist[0]=True
    if Thefield == field:
        checklist[1]=True
    if Thefloor == mapfloor[floor]:
        checklist[2]=True
    if Thestatus == status:
        checklist[3]=True
    print(checklist)
    if checklist == [True,True,True,True]:
        return {'name':room, 'num1':'*','num2':'*', 'status':Thestatus}
    else:
        return None

#  测试用
def default(request):
    return render(request, 'error.html')
#  空教室查询 有一个可随意设置的POST表单提供过滤条件（过滤条件可以在开头的context列表中设计，
#  首次访问页面data是没有数据的，也就不会展示空教室对应的表格）
def inquiry(request):
    context ={"hint":'',"filter":{'build':['品学楼','立人楼'], 'field':["A","B","C"],
                                  "floor":["一层","二层","三层","四层","五层"],
                                  'status':[i[1] for i in ClassroomStatus.CHOICES_STATUS]},
              "data":[]}

    if request.POST:
        print(request.POST)
        date = datetime.datetime.now().date()
        all_classroom = ClassroomStatus.objects.filter(date=date)
        for i in list(all_classroom):
            rtn=filter(request.POST.get('build'), request.POST.get('field'),
                      request.POST.get('floor'), request.POST.get('status'), i )
            if rtn:
                context["data"].append(rtn)
            else:
                continue
        pass

    return render(request, 'inquiry.html', context=context)

#  反馈提交 相关理由都可以自定义，数据库方面没有过滤需求
def feedback(request):
    select_reason_list=["实际用途与申请不符","实际使用时间与申请不符","桌椅损坏","多媒体设备故障","其他"]
    context = {'form': None, "reason_list":select_reason_list, "hint":''}
    if request.POST:
        FeedBack.objects.create(reason=request.POST.get('feedback-select-reason'),
                                text=request.POST.get('feedback-message'))
        context['hint'] = '😄提交成功！请耐心等待工作人员的处理'
    return render(request, 'feedback.html', context)

# 定教室，context也可以自定义
def order(request):
    context = {"hint": '', "classroom_dic": ["品学楼A", "品学楼B", "品学楼C","立人楼A","立人楼B"],
               "apply_time": [i[1] for i in ClassroomApply.CHOICES_TIMEPIERED],
               "apply_reason":["班级自习", "班级活动", "部门活动", "老师调课", "其他"]}
    tz = datetime.timezone(datetime.timedelta(hours=+8))
    if request.POST:
        # print(request.POST)
        classroomID = request.POST.get("select_build")+request.POST.get("local")
        period = request.POST.get("period")
        date = datetime.datetime.now().date()
        print(datetime.datetime.now().astimezone(tz))
        status = check(classroomID,period,date)
        user = request.POST.get("user")
        detail = request.POST.get('order-detail')
        if request.POST.get("submit_btn")=='submit':
            if status == "空闲" or status == "可拼":
                reasondic = {'apply_reason':detail, "deny_reason":''}
                ClassroomApply.objects.create(date=date, classroomID=classroomID,
                                              datetime=datetime.datetime.now().astimezone(tz),
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
# 我的申请页面
def my_request(request):
    if request.user.is_authenticated:
        context={"hint":'',"data":[]}
        tz = datetime.timezone(datetime.timedelta(hours=+8))
        user = request.user
        applylist = ClassroomApply.objects.filter(userID=user)
        print(applylist)
        if applylist.values().first() != None:
            for i in list(applylist):
                context["data"].append({"classroom": i.classroomID,
                                        "datetime": str(i.datetime.astimezone(tz))[:-10],
                                        "status": i.status,
                                        "reason": i.reason['deny_reason']})
            return render(request, 'my_request.html', context=context)
    return render(request, 'my_request.html')

#  申请状态的数据库初始化
def init(request):
    build = ["品学楼A", "品学楼B", "品学楼C","立人楼A","立人楼B"]
    date = datetime.datetime.now().date()
    classroomID = [i+str(j) for i in build for j in range(101,106)]
    period = [i[1] for i in ClassroomApply.CHOICES_TIMEPIERED]
    initdata = [{"date":date, "classroomID":i, "timePeriod":j}
                for i in classroomID for j in period]
    # 先删除所有内容
    ClassroomStatus.objects.all().delete()
    ClassroomApply.objects.all().delete()
    for i in initdata:
        ClassroomStatus.objects.create(date=i['date'],classroomID=i['classroomID'],
                                       timePeriod=i['timePeriod'])
    print("初始化完成")
    return redirect(reverse("index"))