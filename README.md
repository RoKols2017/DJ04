# 🎬 Django Movie Project

Этот проект — простое веб-приложение на Django для добавления фильмов, описаний и отзывов, с красивым интерфейсом на Bootstrap 5.

## 🚀 Стек технологий

- ```Python 3.13````
- ```Django 5.2````
- ```Bootstrap 5````

## 📁 Структура

```
movie_project/
├── films/
│   ├── migrations/
│   ├── templates/
│   │   └── films/
│   │       ├── base.html
│   │       ├── add_film.html
│   │       ├── film_list.html
│   │       └── home.html
│   ├── templatetags/
│   │   ├── __init__.py
│   │   └── form_filters.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── movie_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

## ⚙️ Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/your-username/movie_project.git
   cd movie_project
   ```

2. Создайте виртуальное окружение и активируйте его:
   ```
   python -m venv .venv
   source .venv/bin/activate        # Linux/macOS
   .venv\Scripts\activate           # Windows
   ```

3. Установите зависимости:
   ```
   pip install django
   ```

4. Примените миграции:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Запустите сервер:
   ```
   python manage.py runserver
   ```

## 🌐 Интерфейс

- `/` — стартовая страница
- `/add/` — добавить фильм
- `/list/` — список фильмов

## ✨ Особенности

- Форма с Bootstrap-оформлением
- Отображение всех фильмов с отзывами
- Кастомный шаблонный фильтр: ````add_class```` для Bootstrap
- Интерфейс на русском языке 🇷🇺

## 📦 Поддержка

Проект учебный, но может быть расширен:
- Добавление изображений / постеров
- Оценка фильмов (звёзды)
- Авторизация пользователей

## 📄 Лицензия

Свободное использование для учебных целей. 🧠
