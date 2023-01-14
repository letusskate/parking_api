from django.contrib import admin

from apps.orders.models import Orders


# Register your models here.
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    fields = ['status', 'parkingBeginTime', 'parkingEndTime', 'parkingPlace', 'user']
