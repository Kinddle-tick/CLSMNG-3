from django.db import models

from django.contrib.auth.models import User


class school_timetable(models.Model):
    userID = models.CharField(max_length=64, primary_key=True)
    is_delete = models.BooleanField(default=False)
    data = models.JSONField(null=True)
    def __str__(self):
        return str(self.data)
    class Meta:
        db_table = 'timetable'