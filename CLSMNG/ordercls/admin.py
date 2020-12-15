from django.contrib import admin
# Register your models here.
from ordercls.models import  FeedBack, select, OrderModel, order_select1,order_select2

admin.site.register(FeedBack)
admin.site.register(select)
admin.site.register(OrderModel)
admin.site.register(order_select1)
admin.site.register(order_select2)


