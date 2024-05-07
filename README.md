# Команды для запуска проекта

- **Сборка Docker-образа:**
``docker build -t test_task .``

- **Запуск Docker-контейнера:**
``docker run -p 8080:8080 test_task``

- **Запуск сервера напрямую:**
``python -m backend/main.py``

- **Тестирование проекта с использованием pytest:**
``pytest``

- **Установка зависимостей с помощью Poetry:**
``poetry install``
``poetry shell``

# Использование API

- **GET /healthcheck:**
  - **Описание:** Проверка статуса сервера.
  - **Запрос:** 
    ```
    curl -X GET http://localhost:8080/healthcheck
    ```
  - **Ответ:** Пустой JSON объект и статус 200.

- **POST /hash:**
  - **Описание:** Возвращает SHA-256 хэш строки.
  - **Запрос:** 
    ```
    curl -X POST http://localhost:8080/hash -H "Content-Type: application/json" -d '{"string": "your_string"}'
    ```
  - **Ответ:**
    ```
    {
      "hash_string": "хэш вашего сообщения"
    }
    ```
  - **Ошибки:**
    - Если поле `string` отсутствует:
      ```
      {
        "validation_errors": "Missing required field 'string'"
      }
      ```
    - Статус ответа: 400
