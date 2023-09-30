from django.db import models
from django.utils import timezone


class Product(models.Model):
    """Товары"""
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Наименование')
    category = models.CharField(max_length=50, verbose_name='Категория')
    is_active = models.BooleanField(default=True, verbose_name='Активность товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def previous_month_orders(self) -> int:
        today = timezone.now()
        last_month = today.replace(month=today.month - 1, day=1)
        pmo = OrderProducts.objects.filter(
            order__created_at__month=last_month.month,
            product__id=self.id,
        )
        if pmo:
            return sum(obj.count_product for obj in pmo)

        return 0

    def current_month_orders(self) -> int:
        today = timezone.now()
        cmo = OrderProducts.objects.filter(
            order__created_at__month=today.month,
            product__id=self.id,
        )
        if cmo:
            return sum(obj.count_product for obj in cmo)

        return 0

    def __str__(self):
        return self.title


class Order(models.Model):
    """Заказ"""
    created_at = models.DateTimeField(auto_now_add=False, verbose_name='Дата создания заказа')

    def __str__(self):
        return f'Заказ {self.id} от {self.created_at}'


class OrderProducts(models.Model):
    """Товары в заказе"""
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    count_product = models.IntegerField(default=1, verbose_name='Количество единиц товара')

    def __str__(self):
        return f'Заказ {self.order.id}'
