from django.db import models
import datetime
from django.contrib.auth.models import User

class FeedBack(models.Model):
    """form feedback"""
    # reason = models.ForeignKey(to='select',on_delete=models.CASCADE)
    reason = models.CharField(max_length=200)
    text = models.TextField()
    #date_added = models.DateTimeField(auto_now_add=True)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"reason: {self.reason}  text:{self.text}"

class ClassroomApply(models.Model):
    CHOICES_TIMEPIERED =(
        (0, "第一，二节课"), (1, "第三、四节课"), (2, "第五、六节课"), (3, "第七、八节课"), (4, "第九节课之后"),
    )
    CHOICES_STATUS=(
        (0, "批准"), (1, "未受理"), (2, "拒绝"),
    )
    applyID = models.AutoField(primary_key=True,
                                  auto_created=True)                        # 申请的ID
    datetime = models.DateTimeField(auto_now_add=True)  # 申请时间
    date = models.DateField()                           # 该教室被管理员开放的日期
    classroomID = models.CharField(max_length=20)   # 品学楼A123等
    timePeriod = models.CharField(choices=CHOICES_TIMEPIERED,
                                  max_length=50)    # 时间段

    userID = models.CharField(max_length=200)
    is_read = models.BooleanField(default=False)    # 是否被批阅
    status = models.CharField(choices=CHOICES_STATUS,
                              max_length=30,
                              default="未受理")        # 申请状态
    reason = models.JSONField()
    def __str__(self):
        return f"ID:{self.applyID} userID:{self.userID}, is_read:{self.is_read} status:{self.status} \n" \
               f"applytime:{self.datetime}. Date:{self.date} \nRoom:{self.classroomID} Period:{self.timePeriod}"


class ClassroomStatus(models.Model):
    CHOICES_TIMEPIERED =(
        (0, "第一，二节课"), (1, "第三、四节课"), (2, "第五、六节课"), (3, "第七、八节课"), (4, "第九节课之后"),
    )
    CHOICES_STATUS =(
        (0, "空闲"), (1, "有课"), (2, "有条"), (3, "借出"), (4, "可拼"),
    )
    date = models.DateField(default=datetime.datetime.now().date())      # 该教室被管理员开放的日期
    classroomID = models.CharField(max_length=20)   # 品学楼A123等
    timePeriod = models.CharField(choices=CHOICES_TIMEPIERED,
                                  max_length=50)    # 时间段
    status = models.CharField(choices=CHOICES_STATUS,
                              max_length=30,
                              default="空闲")        # 当前状态
    applyID = models.CharField(max_length=100,
                               null=True,
                               default=None)      # 对应的申请ID 没有则为null， 默认无
    def __str__(self):
        return f"Date:{self.date} Room:{self.classroomID} Period:{self.timePeriod} Status:{self.status}"





# class OrderModel(models.Model):
#     """form feedback"""
#     申请教室 = models.TextField()
#     申请时间 = models.ForeignKey(to='order_select1',on_delete=models.CASCADE)
#     申请理由 = models.ForeignKey(to='order_select2',on_delete=models.CASCADE)
#     申请单位 = models.TextField()
#     是否可拼教室 = models.TextField()
#
#     def __str__(self):
#         return self.申请教室
#
# class select(models.Model):
#     name = models.CharField(max_length =200)
#     def __str__(self):
#         return self.name
#
# class order_select1(models.Model):
#     name = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name
#
# class order_select2(models.Model):
#     name = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name

