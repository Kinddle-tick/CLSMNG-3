from django.db import models

from django.contrib.auth.models import User

#  三部分 使用者ID，课程表是否被删除（软删除），特定的课程表保存格式JSON
class school_timetable(models.Model):
    userID = models.CharField(max_length=64, primary_key=True)
    is_delete = models.BooleanField(default=False)
    data = models.JSONField(null=True)
    def __str__(self):
        return str(self.data)
    class Meta:
        db_table = 'timetable'