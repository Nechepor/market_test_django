# market_test_django


Склонируйте репозиторий на свой компьютер:

```bash
git clone https://github.com/Nechepor/market_test_django.git
```

Для запуска с помощью docker-compose:
   - Проверьте значение DEV_MODE в .env - должно быть False
   - Проверьте Чтобы docker-compose.yml не содержал в себе закомментированный web
   - Перейдите в директорию, куда склонировали проект.
   - Выполните команду docker-compose up. По дефолту, суперюзер будет с данными admin\password
   - Все таблицы будут заполнены данными с помощью команды products_table/management/commands/populate_db.py
   - Проект доступен по 127.0.0.1:8000
   - /login - авторизация
   - /register - регистрация
   - /market/product-list - список товаров
   - /admin - админка
