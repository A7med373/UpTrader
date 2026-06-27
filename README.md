# Django Tree Menu

Django-приложение с древовидным меню, которое хранится в базе данных, редактируется через админку и рендерится на страницах через template tag.

Проект сделан как backend-задача: важно не оформление меню, а корректная модель данных, определение активного пункта, эффективная выборка из БД и понятный запуск.

## Возможности

- Меню хранится в БД.
- Пункты меню редактируются через стандартную Django admin.
- Меню рендерится через template tag.
- Активный пункт определяется по текущему URL.
- На одной странице можно использовать несколько меню по названию.
- Раскрываются родители активного пункта и первый уровень вложенности под ним.
- На отрисовку одного меню выполняется один запрос к БД.

## Стек

- Python
- Django
- PostgreSQL
- Docker, Docker Compose
- Nginx
- Gunicorn

## Запуск через Docker

Создайте файл `.env`:

```env
SECRET_KEY=change-me
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=uptrader
SQL_USER=uptrader
SQL_PASSWORD=uptrader
SQL_HOST=db
SQL_PORT=5432
```

Запустите проект:

```bash
docker compose up --build
```

Приложение будет доступно по адресу:

```text
http://localhost
```

## Локальный запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Тесты

```bash
python manage.py test
```

## Ключевые файлы

```text
tree_menu/models.py              - модель пункта меню
tree_menu/templatetags/menu_tags.py - template tag для отрисовки
tree_menu/admin.py               - управление меню в админке
templates/                       - страницы для проверки вложенных URL
docker-compose.yml               - запуск web, db и nginx
```

## Что демонстрирует проект

- Работа с иерархическими данными в Django.
- Оптимизация количества запросов к базе.
- Использование template tags.
- Docker-окружение для Django + PostgreSQL + Nginx.
