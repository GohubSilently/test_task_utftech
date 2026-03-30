# Тестовое задание для UTF.Tech

[![Python](https://img.shields.io/badge/-Python_3.13-3771a1?style=flat&logo=Python&logoColor=ffffff)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django_6.0.3-092e20?style=flat&logo=Django&logoColor=ffffff)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/-Django%20REST%20Framework_3.17-96000e?style=flat&logo=django&logoColor=ffffff)](https://www.django-rest-framework.org/)

Автор - [Халин Вадим](https://t.me/gohub1)

---

## Оглавление:
- [Описание](#описание)
- [Структура проекта](#структура-проекта)
- [Технологии](#технологии)
- [Локальный запуск](#локальный-запуск)

---

## Описание:
Исправлены некоторые поля в моделях, которые давались изначально.
Например: **IntegerField** на **PositiveIntegerField**;<br>
Поменял поле **additional** сериализатор **FoodSerializer**, для того, чтобы блюда,
у которых (is_publish=False), не показывались в additional.
Админ панель, добавил фильтрацию по стоимости и удобное отображение всех полей.

---

## Структура проекта:
```text
|── .gitignore
├── README.md
└── backend
    ├── api
    │   ├── migrations
    │   │   ├── __init__.py
    │   ├── tests
    │   │   ├── __init__.py
    │   │   ├── conftest.py
    │   │   ├── factories.py
    │   │   └── test_food_list.py
    │   ├── __init__.py
    │   ├── apps.py
    │   ├── serializers.py
    │   ├── urls.py
    │   └── views.py
    ├── data
    │   ├── food.json
    │   └── foodcategory.json
    ├── food
    │   ├── management
    │   │   └── commands
    │   │       ├── create_superuser.py
    │   │       ├── import_data.py
    │   │       ├── load_food.py
    │   │       └── load_foodcategory.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── constants.py
    │   └── models.py
    ├── utftech
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── .env.excample
    ├── .python-version
    ├── manage.py
    ├── pyproject.toml
    └── uv.lock
```

---

## Технологии:
- Python
- Django / DRF
- Pytest

---

## Локальный запуск:
1. Клонируем репозиторий.
```
git clone git@github.com:GohubSilently/test_task_utftech.git
cd test_task_utftech && cd backend
```

2. Создаем .env.
```
SECRET_KEY=super-secret-password
DEBUG=TRUE
ALLOWED_HOSTS='127.0.0.1 localhost'

POSTGRES_DB=utftech
POSTGRES_USER=utftech_user
POSTGRES_PASSWORD=utftech_password
DB_HOST=db
DB_PORT=5432
```

3. Применяем миграции и загружаем данные.
```
uv run manage.py migrate && uv run manage.py createsuperuser
uv run manage.py load_foodcategory && uv run manage.py load_food
```

4. Запускаем проект
```
uv run manage.py runserver
```

Переходим на endpoint - [Ссылка](http://127.0.0.1:8000/api/v1/foods/)

---
