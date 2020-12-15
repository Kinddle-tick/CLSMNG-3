# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # Author:Kinddle
# import os
# import django
#
# import pymysql
# pymysql.version_info=(1,4,13,"final",0)
# pymysql.install_as_MySQLdb()
#
# # from django.conf import settings
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
# django.setup()
# # from ..timetable.models import school_timetable
# from CLSMNG.timetable.models import school_timetable
#
# timetb_init=[{'userID': '0001', 'is_delete': False, 'data':{
#     '1':["学术英语", ["1-3:4"]], '2':['信号与系统', ["1-5:6", "3-3:4", "5-3:4"]], '3':['微嵌', ["2-1:2", "4-5:6", "5-1:2"]],
#     '4':['游泳', "2-3:4"], '5':["计算机通信网", ["2-5:6", "4-1:2"]], '6':["专业写作与表达", "2-9:10"],
#     '7':["顶点计划", "3-5:6"], '8':["大物实验(单)", "4-3:4,odd"], '9':["电工电气", "4-9:12"]
# }},
#              {'userID':'0002', 'is_delete': False, 'data':{
#     '1':["学术英语", ["1-3:4"]], '2':['信号与系统', ["1-5:6", "3-3:4", "5-3:4"]], '3':['微嵌', ["2-1:2", "4-5:6", "5-1:2"]],
#     '4':['游泳', "2-3:4"], '5':["计算机通信网", ["2-5:6", "4-1:2"]], '6':["专业写作与表达", "2-9:10"],
#     '7':["顶点计划", "3-5:6"], '8':["大物实验(双)", "4-3:4,even"], '9':["电工电气", "4-9:12"]
# }},
#              ]
# #  删除所有数据
# timetb = school_timetable.object.all().delete()
#
# #  按照设定的初始设计初始化
#
# for i in timetb:
#     status=school_timetable.object.create(userID=i['userID'], is_delete=i['is_delete'], data=i["data"])
#     print(status)