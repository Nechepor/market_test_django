from django.core.management.base import BaseCommand
from django.db import transaction
from products_table.models import Product, Order, OrderProducts

from random import randint


class Command(BaseCommand):
    help = 'Заполнить базу данных данными'

    def handle(self, *args, **kwargs):

        Product.objects.bulk_create([
            Product(1, 'Товар 1', 'Категория A', True, 9.99),
            Product(2, 'Товар 2', 'Категория B', True, 19.99),
            Product(3, 'Товар 3', 'Категория A', True, 29.99),
            Product(4, 'Товар 4', 'Категория B', True, 14.99),
            Product(5, 'Товар 5', 'Категория A', True, 24.99)
        ])

        Order.objects.bulk_create([
            Order(1, '2023-08-01'),
            Order(2, '2023-08-02'),
            Order(3, '2023-08-03'),
            Order(4, '2023-08-04'),
            Order(5, '2023-08-05'),
            Order(6, '2023-09-01'),
            Order(7, '2023-09-02'),
            Order(8, '2023-09-03'),
            Order(9, '2023-09-04'),
            Order(10, '2023-09-05'),
            Order(11, '2023-10-01'),
            Order(12, '2023-10-02'),
            Order(13, '2023-10-03'),
            Order(14, '2023-10-04'),
            Order(15, '2023-10-05'),
        ])

        num_records = 100
        with transaction.atomic():
            for i in range(1, num_records):
                order_product = OrderProducts(
                    id=i,
                    order=Order.objects.get(pk=randint(1, 15)),
                    product=Product.objects.get(pk=randint(1, 5)),
                    count_product=randint(1, 10)
                )
                order_product.save()

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена.'))
