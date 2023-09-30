from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Заполнить базу данных данными'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            sql_script = """
            INSERT INTO products_table_product (title, category, is_active, price)
            VALUES
                    ('Товар 1', 'Категория A', true, 9.99),
                    ('Товар 2', 'Категория B', true, 19.99),
                    ('Товар 3', 'Категория A', true, 29.99),
                    ('Товар 4', 'Категория B', true, 14.99),
                    ('Товар 5', 'Категория A', true, 24.99);

            INSERT INTO products_table_order (created_at)
            VALUES
                    ('2023-08-01'::date),
                    ('2023-08-02'::date),
                    ('2023-08-03'::date),
                    ('2023-08-04'::date),
                    ('2023-08-05'::date),
                
                    ('2023-09-01'::date),
                    ('2023-09-02'::date),
                    ('2023-09-03'::date),
                    ('2023-09-04'::date),
                    ('2023-09-05'::date),
                
                    ('2023-10-01'::date),
                    ('2023-10-02'::date),
                    ('2023-10-03'::date),
                    ('2023-10-04'::date),
                    ('2023-10-05'::date);



            INSERT INTO products_table_orderproducts (order_id, product_id, count_product)
            SELECT
                o.id AS order_id,
                p.id AS product_id,
                ROUND(RANDOM() * 10)::int AS count_product
            FROM products_table_order o
            CROSS JOIN products_table_product p;
            """

            cursor.execute(sql_script)
            self.stdout.write(self.style.SUCCESS('База данных успешно заполнена.'))