from django.contrib import admin
# Register your models here.
from ordercls.models import FeedBack,ClassroomStatus,ClassroomApply

admin.site.register(FeedBack)
admin.site.register(ClassroomStatus)
admin.site.register(ClassroomApply)


