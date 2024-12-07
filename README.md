## Описание

Movie API — это приложение для управления пользователями и их любимыми фильмами. С помощью этого API пользователи могут добавлять фильмы в свои избранные и просматривать список избранного.


## Установка

1. **Клонировать репозиторий**

   ```bash
   git clone git@github.com:EgorIvanov96/film_library.git
   ```

2. **Создать виртуальное окружение**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   ```

3. **Установить зависимости**

   ```bash
   pip install -r requirements.txt
   ```

4. **Создайте в корне проекта файл .env для испольщования PostgreSQL или используйте SQLite**

    ```
    POSTGRES_USER=django_user 
    POSTGRES_PASSWORD=mysecretpassword
    OSTGRES_DB=django
    DB_HOST=db
    DB_PORT=5432
    ```
4. **Применить миграции**

   ```bash
   python manage.py migrate
   ```

5. **Запустить сервер**

   ```bash
   python manage.py runserver
   ```

Теперь ты можешь использовать API по адресу `http://127.0.0.1:8000/`


## Использование API

### Пользователи

- **POST /users/** - Создать пользователя
- **GET /users/** - Получить список пользователей
- **GET /users/{id}/** - Получить пользователя по ID
- **DELETE /users/{id}/** - Удалить пользователя (можно только своего)

### Фильмы

- **POST /movies/** - Создать фильм
- **GET /movies/** - Получить список фильмов
- **GET /movies/{id}/** - Получить информацию о фильме по ID
- **DELETE /movies/{id}/** - Удалить фильм

### Избранное

- **POST /movies/{id}/favorite/** - Добавить фильм в избранное
- **DELETE /movies/{id}/favorite/** - Удалить фильм из избранного
- **GET /movies/list_favorite/** - Получить список избранных фильмов