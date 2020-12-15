from django.db import models

from django.contrib.auth.models import User

# # Create your models here.
# class Topic(models.Model):
#     """用户学习的主题"""
#     text = models.CharField(max_length=200)
#     date_added = models.DateTimeField(auto_now_add=True)
#     owner = models.ForeignKey(User, on_delete = models.CASCADE)
#     def __str__(self):
#         """返回模型的字符串表示"""
#         return self.text
#
#
# class Entry(models.Model):
#     """below topic"""
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     test = models.ForeignKey(to='select',on_delete=models.CASCADE)
#     text = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         """没有则为entrys"""
#         verbose_name_plural = 'entries'
#
#     def __str__(self):
#         """返回模型的字符串表示"""
#         return self.text[:50] + "..."


class FeedBack(models.Model):
    """form feedback"""
    # reason = models.ForeignKey(to='select',on_delete=models.CASCADE)
    reason = models.CharField(max_length=200)
    text = models.TextField()
    #date_added = models.DateTimeField(auto_now_add=True)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class OrderModel(models.Model):
    """form feedback"""
    申请教室 = models.TextField()
    申请时间 = models.ForeignKey(to='order_select1',on_delete=models.CASCADE)
    申请理由 = models.ForeignKey(to='order_select2',on_delete=models.CASCADE)
    申请单位 = models.TextField()
    是否可拼教室 = models.TextField()

    def __str__(self):
        return self.申请教室

class select(models.Model):
    name = models.CharField(max_length =200)
    def __str__(self):
        return self.name

class order_select1(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class order_select2(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

