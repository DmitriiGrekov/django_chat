
# Backend Чата с использование WebSocket


Разворачивание проекта

1) Склонировать репозиторий
2) в папке репозитория выполнить команду: python -m venv env
3) активировать виртуальное окружение:

    cd env/scripts

    activate
4) установить зависимости:

    pip install -r requirements.txt
5) выполнить миграции

    python manage.py migrate
6) создать суперпользователя

    python manage.py createsuperuser
7) запустить сервер

    daphne config.asgi:application