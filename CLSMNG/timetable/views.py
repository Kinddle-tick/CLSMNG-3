from django.shortcuts import render

# from .models import Topic, Entry

from django.http import HttpResponseRedirect, Http404

from django.urls import reverse

# from .forms import TopicForm, EntryForm, FeedBackForm, OrderForm

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'index.html')

# @login_required
# def topics(request):
#     """显示所以主题"""
#     topics = Topic.objects.filter(owner=request.user).order_by('date_added')
#     #topics = Topic.objects.order_by('date_added')
#     context = {'topics': topics}
#     return render(request, 'topics.html', context)

# @login_required
# def new_entry(request, topic_id):
#     """在特定主题中添加条目"""
#     topic = Topic.objects.get(id=topic_id)
#
#     if request.method != 'POST':
#         # 未提交的数据：创建一个表单
#         form = EntryForm()
#     else:
#         # post提交的数据，对数据进行处理
#         form = EntryForm(data=request.POST)
#         if form.is_valid():
#             new_entry = form.save(commit=False)
#             new_entry.topic = topic
#             new_entry.save()
#             return HttpResponseRedirect(reverse('timetable:topic', args=[topic_id]))
#     context = {'topic': topic, 'form': form}
#     return render(request, 'new_entry.html', context)
#

# @login_required
# def edit_entry(request, entry_id):
#     """编辑既有条目"""
#     entry = Entry.objects.get(id=entry_id)
#     topic = entry.topic
#     if topic.owner!=request.user:
#         return Http404
#
#     if request.method != 'POST':
#         # 初次请求，使用当前的条目填充表单
#         form = EntryForm(instance=entry)
#     else:
#         # post提交的数据，对数据进行处理
#         form = EntryForm(instance=entry, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('timetable:topic', args=[topic.id]))
#
#     context = {'entry': entry, 'topic': topic, 'form': form}
#     return render(request, 'edit_entry.html', context)

# @login_required
# def topic(request, topic_id):
#     """显示单个主题及其所有的条目"""
#     topic = Topic.objects.get(id=topic_id)
#     if topic.owner!=request.user:
#         return Http404
#     entries = topic.entry_set.order_by('-date_added')
#     context = {'topic': topic, 'entries': entries}
#     return render(request, 'topic.html', context)

# @login_required
# def new_topic(request):
#     """添加新主题"""
#     if request.method != 'POST':
#         form = TopicForm()
#     else:
#         form = TopicForm(request.POST)
#         if form.is_valid():
#             new_topic = form.save(commit=False)
#             new_topic.owner = request.user
#             new_topic.save()
#             return HttpResponseRedirect(reverse('timetable:topics'))
#     context = {'form': form}
#     return render(request, 'new_topic.html', context)


# @login_required
# def feedback2(request):
#     """学习笔记的主页"""
#     if request.method!= 'post':
#         form = FeedBackForm()
#     else:
#         form = FeedBackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('timetable:index'))
#     context = {'form':form}
#     return render(request, 'feedback.html',context)

@login_required
def kongjiaoshichakan(request):
    return  render(request,'kongjiaoshichakan.html')



@login_required
def find3(request):
    return  render(request,'find3.html')

@login_required
def find4(request):
    return  render(request,'find4.html')

@login_required
def school_timetable(request):
    return  render(request,'school_timetable.html')

@login_required
def search(request):
    return  render(request,'search.html')


# def feedback(request):
#     """modelsform版本"""
#     if request.method !='POST':
#         form = FeedBackForm()
#     else:
#         form = FeedBackForm(request.POST)
#         form.save()
#         return HttpResponseRedirect(request)
#     context = {'form':form}
#     return render(request, 'feedback.html',context)

# def order(request):
#     """modelsform版本"""
#     if request.method != 'POST':
#         form = OrderForm()
#     else:
#         form = OrderForm(request.POST)
#         form.save()
#         return HttpResponseRedirect(request)
#     context = {'form': form}
#     return render(request, 'order.html', context)