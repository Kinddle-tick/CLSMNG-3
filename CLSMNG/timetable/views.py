from django.shortcuts import render, redirect, reverse
from django.forms.models import model_to_dict
from .models import school_timetable as st

from django.http import HttpResponseRedirect, Http404

from django.urls import reverse

# from .forms import TopicForm, EntryForm, FeedBackForm, OrderForm

from django.contrib.auth.decorators import login_required
import re
def school_table_decode(table:dict):
    color_list=["#FFFFCC", "#CCFFFF", "#FFCCCC", "#FFCC99", "#FFFF99", "#99CC99"]
    context=[{"index": i+1, "text":[{"text":'',"color":"#ffffff", 'property':None} for j in range(7)] } for i in range(12)]
    print(table.keys())
    for i in table.keys():
        data = table[i]
        decorate_color = color_list[int(i)%len(color_list)]
        text = data[0]
        print(data)
        if type(data[1])==str:# 虽然这里允许在记录里不使用列表 但还是建议使用列表表示课程的时间
            data[1]=[data[1]]
        for record in data[1]:
            try:
                record, odd_even = re.split(',',record)
            except Exception:
                #区分单双周的部分并没有完成， 但是代码我留在这了
                pass

            col=int(record[0])-1
            startline,endline=re.split(':',record[2:])
            for line in range(int(startline),int(endline)+1):
                if line==int(startline):
                    context[line-1]["text"][col]["text"]=text
                context[line-1]["text"][col]["color"] = decorate_color

    return context


def school_timetable(request):
    default_use='0001'
    try:
        table = st.objects.get(userID=default_use)
        tabledic=model_to_dict(table)
    except Exception as z:
        #  未找到数据显示空白表
        # print('error'+z)
        context = school_table_decode({})
        return render(request, 'school_timetable.html', context={"data":context})
    context = school_table_decode(tabledic['data'])
    return render(request, 'school_timetable.html', context={"data":context})

@login_required
def search(request):
    return render(request, 'index.html')





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
