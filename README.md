# EdTech

## Описание

Тестовое задание.

## Автор:

[Александр Лобачев](https://github.com/AlexandrLobachev/)

## Технологии используемые в проекте:

Python, Django, DRF

## Как запустить проект локально:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:AlexandrLobachev/EdTech.git
```
```
cd EdTech
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
cd backend
```
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```
Проект доступен по адресу:

> http://127.0.0.1:8000/

## Примеры работы API:
### Получение списка курсов:


#### Пример запроса на получение списка постов:
GET http://127.0.0.1:8000/api/courses/
```
[
    {
        "name": "Фронтенд разработка",
        "description": "Разработка фронтенда на JS",
        "start_date": "2024-03-10T00:00:00Z",
        "price": 50000,
        "qty_lessons": 2,
        "qty_students": 3,
        "filling": 75.0,
        "popularity": 60.0
    },
    {
        "name": "Бэкенд разработка",
        "description": "Разработка бэкенда на Python",
        "start_date": "2024-03-02T21:35:29Z",
        "price": 70000,
        "qty_lessons": 0,
        "qty_students": 1,
        "filling": "Групп не сформировано",
        "popularity": 20.0
    }
]
``````

#### Пример запроса на получение списка уроков по выбранному курсу:
Доступен только авторизованным пользователям, у которых есть досиуп к курсу.


GET http://127.0.0.1:8000/api/courses/1/lessons/
```
[
    {
        "name": "1. Вводный урок FRON"
    },
    {
        "name": "2. Второй урок FRON"
    }
]
``````