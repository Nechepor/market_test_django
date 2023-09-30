from django.contrib import admin

from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'prev_month', 'curr_month']

    def prev_month(self, obj):
        return obj.previous_month_orders()
    prev_month.short_description = 'Количество заказов в предыдущем месяце'

    def curr_month(self, obj):
        return obj.current_month_orders()
    curr_month.short_description = 'Количество заказов в текущем месяце'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderProducts)
class OrderProductsAdmin(admin.ModelAdmin):
    pass
