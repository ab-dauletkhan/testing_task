# Команды для запуска проекта

- **Сборка Docker-образа:**
``docker build -t test_task .``

- **Запуск Docker-контейнера:**
``docker run -p 8080:8080 test_task``

- **Запуск сервера напрямую:**
``python -m backend.main``

- **Тестирование проекта с использованием pytest:**
``pytest``

- **Установка зависимостей с помощью Poetry:**
``poetry install``
``poetry shell``
