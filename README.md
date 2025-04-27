# Django Tree Menu

## Описание проекта

Django-приложение, реализующее древовидное меню со следующими возможностями:

- Меню реализовано через template tag
- Все пункты выше выделенного пункта развернуты
- Первый уровень вложенности под выделенным пунктом тоже развернут
- Хранится в БД
- Редактируется в стандартной админке Django
- Активный пункт меню определяется исходя из URL текущей страницы
- На одной странице может быть несколько меню, определяемых по названию
- При клике на меню происходит переход по заданному URL (явному или через named url)
- На отрисовку каждого меню требуется ровно 1 запрос к БД

## Project Description

## Технологический стек 

- Python 3.10+
- Django 5.2
- PostgreSQL 14 (для Docker-установки)
- SQLite (для локальной разработки) 
- Docker & Docker Compose
- Nginx (для Docker-установки) 
- Gunicorn

## Установка и запуск 

### Локальная установка 

1. Клонировать репозиторий:

```bash
git clone https://github.com/A7med373/UpTrader.git
cd UpTrader
```

2. Создать и активировать виртуальное окружение:
3. 
```bash
# Linux/macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. Установить зависимости:

```bash
pip install -r requirements.txt
```

4. Применить миграции:

```bash
python manage.py migrate
```

5. Создать суперпользователя:

```bash
python manage.py createsuperuser
```

6. Заполнить базу данных тестовыми данными (опционально):
```bash
python populate_menu_data.py
```

7. Запустить сервер разработки:

```bash
python manage.py runserver
```

8. Открыть в браузере: http://127.0.0.1:8000/

### Установка с использованием Docker 

1. Клонировать репозиторий:

```bash
git clone https://github.com/A7med373/UpTrader.git
cd UpTrader
```

2. Создать файл .env на основе .env.example:

```bash
cp .env.example .env
```

3. Отредактировать .env файл, установив нужные значения.

4. Запустить контейнеры:

```bash
docker-compose up -d --build
```

5. Открыть в браузере: http://localhost/

> **Примечание**: При запуске через Docker, миграции, создание суперпользователя и заполнение тестовыми данными происходит автоматически согласно настройкам в .env файле.
>

## Использование

### Создание меню в админке

1. Войдите в интерфейс администратора Django 
2. Создайте новое меню с уникальным именем
3. Добавьте объекты MenuItem в меню:
   - Укажите имя для каждого пункта
   - Установите URL (может быть явным URL, например '/about/', или именованным URL, например 'about') 
   - Отметьте 'Is Named URL', если используете именованный URL
   - Установите родительский элемент для вложенных пунктов меню (или оставьте пустым для элементов верхнего уровня)

### Использование шаблонного тега

1. Загрузите теги меню в вашем шаблоне:

```html
{% load menu_tags %}
```

2. Используйте тег draw_menu с именем вашего меню:

```html
{% draw_menu 'main_menu' %}
```

Вы можете иметь несколько меню на одной странице:

```html
{% draw_menu 'main_menu' %}
{% draw_menu 'footer_menu' %}
```
## Пример

```html
{% load menu_tags %}

<div class="sidebar-menu">
    <h3>Главная навигация / Main Navigation</h3>
    {% draw_menu 'main_menu' %}
</div>
```

## Тестовые данные 

Чтобы заполнить базу данных тестовыми данными меню, выполните:
```bash
python populate_menu_data.py
```

Этот скрипт создаст:

1. Основное меню с иерархией глубиной до 5 уровней, включая:
   - Home, About, Services, Contact как элементы верхнего уровня
   - Множество вложенных элементов под Services (Web Development, Mobile Development и т.д.)
   - Элементы глубиной до 5 уровней (например, Services > Web Development > Frontend > React > React Hooks)
   
2. Вторичное меню с:
   - Resources, Blog, FAQ, Support как элементы верхнего уровня
   - Элементы глубиной до 5 уровней (например, Resources > Documentation > API Documentation > REST API > Authentication) 
   
Тестовые данные включают как именованные URL (например, 'home', 'about'), так и явные URL (например, '/services/#web')



### Переменные окружения

В файле `.env` можно настроить следующие переменные окружения / The following environment variables can be configured in the `.env` file:

- `DEBUG`: Установите "True" для разработки, "False" для продакшена / Set to "True" for development, "False" for production
- `SECRET_KEY`: Секретный ключ Django / Django secret key
- `ALLOWED_HOSTS`: Список разрешенных хостов, разделенных запятыми / Comma-separated list of allowed hosts
- `SQL_ENGINE`: Движок базы данных (по умолчанию: django.db.backends.postgresql) / Database engine (default: django.db.backends.postgresql)
- `SQL_DATABASE`: Имя базы данных / Database name
- `SQL_USER`: Пользователь базы данных / Database user
- `SQL_PASSWORD`: Пароль базы данных / Database password
- `SQL_HOST`: Хост базы данных / Database host
- `SQL_PORT`: Порт базы данных / Database port
- `DJANGO_SUPERUSER_USERNAME`: Имя пользователя администратора (создается при запуске) / Admin username (created on startup)
- `DJANGO_SUPERUSER_EMAIL`: Email администратора / Admin email
- `DJANGO_SUPERUSER_PASSWORD`: Пароль администратора / Admin password
- `LOAD_INITIAL_DATA`: Установите "true" для загрузки тестовых данных при запуске / Set to "true" to load sample data on startup

## CI/CD

### Обзор рабочего процесса

CI/CD pipeline запускается при:
- Push в ветки `main` или `dev`
- Pull requests в ветки `main` или `dev`
- 
### Задачи

Рабочий процесс включает следующие задачи:

1. **Lint**: Проверяет качество и стиль кода 
   - Запускает flake8 для проверки синтаксических ошибок Python и неопределенных имен 
   - Проверяет форматирование кода с помощью black
   - Проверяет сортировку импортов с помощью isort 

2. **Security**: Проверяет наличие уязвимостей безопасности 
   - Сканирует зависимости на наличие известных проблем безопасности с помощью safety 
   
3. **Test**: Запускает набор тестов 
   - Настраивает базу данных PostgreSQL для тестирования 
   - Запускает pytest для выполнения набора тестов
   - Запускается только если проверки lint и security пройдены 

4. **Docker**: Собирает и тестирует Docker-образ 
   - Собирает Docker-образ, используя Dockerfile проекта
   - Проверяет, что образ может быть успешно запущен
   - Запускается только если проверки lint и security пройдены

### Локальный запуск

Вы можете запустить те же проверки локально перед отправкой кода 
```bash
# Установка зависимостей для разработки 
pip install flake8 black isort pytest pytest-django safety

# Запуск проверок линтинга 
flake8 .
black --check .
isort --check .

# Запуск проверок безопасности 
safety check

# Запуск тестов 
pytest

# Сборка и тестирование Docker-образа 
docker build -t uptrader:test .
docker run --rm uptrader:test echo "Docker image built successfully"
```
