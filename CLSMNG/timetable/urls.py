from django.conf.urls import url
from django.urls import path
from . import views
from django.views.static import serve

app_name='time_table'
urlpatterns = [
# 主页
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic, name='topic'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,name='edit_entry'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    url(r'^feedback/$', views.feedback,name = 'feedback'),
    url(r'^kongjiaoshichakan/$',views.kongjiaoshichakan,name = 'kongjiaoshichakan'),
    # url(r'^lesson/$',views.lesson,name = 'lesson'),
    url(r'^order/$',views.order,name = 'order'),
    # url(r'^search/$',views.search,name = 'search'),
    url(r'^school_timetable/$',views.school_timetable,name = 'school_timetable'),
    #url(r'^(?P<path>.*)$', serve, {'document_root': 'timetable/templates/timetable/static'}),


]
