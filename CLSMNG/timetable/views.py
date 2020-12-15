from django.shortcuts import render, redirect, reverse

from .models import school_timetable as st

from django.http import HttpResponseRedirect, Http404

from django.urls import reverse

# from .forms import TopicForm, EntryForm, FeedBackForm, OrderForm

from django.contrib.auth.decorators import login_required


def school_timetable(request):
    default_use='0001'
    try:
        table = st.objects.get(userID=default_use)
        print("timetable")
        print(table)
    except Exception as z:
        #  未找到数据显示空白表
        print(z)
        return render(request, 'school_timetable.html')

    return  render(request,'school_timetable.html')

@login_required
def search(request):
    return  render(request,'search.html')

def init(request):
    timetb_init = [{'userID': '0001', 'is_delete': False, 'data': {
        '1': ["学术英语", ["1-3:4"]], '2': ['信号与系统', ["1-5:6", "3-3:4", "5-3:4"]], '3': ['微嵌', ["2-1:2", "4-5:6", "5-1:2"]],
        '4': ['游泳', "2-3:4"], '5': ["计算机通信网", ["2-5:6", "4-1:2"]], '6': ["专业写作与表达", "2-9:10"],
        '7': ["顶点计划", "3-5:6"], '8': ["大物实验(单)", "4-3:4,odd"], '9': ["电工电气", "4-9:12"]
    }},
                   {'userID': '0002', 'is_delete': False, 'data': {
                       '1': ["学术英语", ["1-3:4"]], '2': ['信号与系统', ["1-5:6", "3-3:4", "5-3:4"]],
                       '3': ['微嵌', ["2-1:2", "4-5:6", "5-1:2"]],
                       '4': ['游泳', "2-3:4"], '5': ["计算机通信网", ["2-5:6", "4-1:2"]], '6': ["专业写作与表达", "2-9:10"],
                       '7': ["顶点计划", "3-5:6"], '8': ["大物实验(双)", "4-3:4,even"], '9': ["电工电气", "4-9:12"]
                   }},
                   ]
    #  删除所有数据
    st.objects.all().delete()
    #  按照设定的初始设计初始化
    for i in timetb_init:
        status = st.objects.create(userID=i['userID'], is_delete=i['is_delete'], data=i["data"])
        print(status)
    return redirect(reverse("index"))
