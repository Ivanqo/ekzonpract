<h1 align="center">Цифровой строительный паспорт - Backend API</h1>

<h2 align="center">Django REST Framework Implementation</h2>

<div align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white" alt="JWT">
</div>

<h2>📝 Описание задачи</h2>

<p>Разработать backend-часть для системы "Цифровой строительный паспорт" со следующими требованиями:</p>

<ul>
  <li>RESTful API для управления строительными проектами</li>
  <li>Две роли пользователей: редактор (полный доступ) и читатель (только просмотр)</li>
  <li>Аутентификация с использованием JWT-токенов</li>
  <li>Хранение данных в PostgreSQL</li>
  <li>Основные операции CRUD для проектов</li>
</ul>

<h3>Модель данных</h3>
<ul>
  <li><strong>Проект</strong>: название, статус, документы (JSON), даты создания/обновления</li>
  <li><strong>Пользователь</strong>: стандартные поля + роль (editor/viewer)</li>
</ul>

<h2>🚀 Описание решения</h2>

<h3>Технологический стек</h3>
<ul>
  <li><strong>Python 3</strong> - основной язык разработки</li>
  <li><strong>Django</strong> - веб-фреймворк</li>
  <li><strong>Django REST Framework</strong> - для построения API</li>
  <li><strong>PostgreSQL</strong> - серверная база данных</li>
  <li><strong>Simple JWT</strong> - аутентификация по токенам</li>
</ul>

<h3>Основные компоненты системы</h3>

<pre><code>construction_passport/
├── api/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py          # Модели User и Project
│   ├── permissions.py     # Кастомные разрешения
│   ├── serializers.py     # Сериализаторы
│   ├── urls.py           # Маршруты API
│   └── views.py          # ViewSets
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py       # Настройки проекта
│   ├── urls.py          # Главные URL-ы
│   └── wsgi.py
└── manage.py
</code></pre>

<h3>API Endpoints</h3>

<table>
  <tr>
    <th>Endpoint</th>
    <th>Method</th>
    <th>Description</th>
    <th>Permissions</th>
  </tr>
  <tr>
    <td><code>/token/</code></td>
    <td>POST</td>
    <td>Получение JWT токена</td>
    <td>Все</td>
  </tr>
  <tr>
    <td><code>/token/refresh/</code></td>
    <td>POST</td>
    <td>Обновление токена</td>
    <td>Аутентифицированные</td>
  </tr>
  <tr>
    <td><code>/projects/</code></td>
    <td>GET</td>
    <td>Список проектов</td>
    <td>Аутентифицированные</td>
  </tr>
  <tr>
    <td><code>/projects/</code></td>
    <td>POST</td>
    <td>Создание проекта</td>
    <td>Редакторы</td>
  </tr>
  <tr>
    <td><code>/projects/{id}/</code></td>
    <td>GET</td>
    <td>Детали проекта</td>
    <td>Аутентифицированные</td>
  </tr>
  <tr>
    <td><code>/projects/{id}/</code></td>
    <td>PUT/PATCH</td>
    <td>Обновление проекта</td>
    <td>Редакторы</td>
  </tr>
  <tr>
    <td><code>/projects/{id}/</code></td>
    <td>DELETE</td>
    <td>Удаление проекта</td>
    <td>Редакторы</td>
  </tr>
</table>

<h2>🛠 Установка и запуск</h2>

<h3>Предварительные требования</h3>
<ul>
  <li>Python 3.8+</li>
  <li>PostgreSQL</li>
  <li>Poetry (рекомендуется) или pip</li>
</ul>

<h3>Инструкция по установке</h3>

<ol>
  <li>Клонировать репозиторий:
<pre><code>git clone https://github.com/yourusername/construction-passport-api.git
cd construction-passport-api</code></pre>
  </li>
  
  <li>Установить зависимости:
<pre><code>poetry install  # или pip install -r requirements.txt</code></pre>
  </li>
  
  <li>Настроить базу данных в <code>config/settings.py</code>:
<pre><code>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'construction_passport',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}</code></pre>
  </li>
  
  <li>Применить миграции:
<pre><code>python manage.py migrate</code></pre>
  </li>
  
  <li>Создать суперпользователя:
<pre><code>python manage.py createsuperuser</code></pre>
  </li>
  
  <li>Запустить сервер:
<pre><code>python manage.py runserver</code></pre>
  </li>
</ol>

<h2>🧪 Тестирование</h2>

<p>Для тестирования API можно использовать Postman или curl:</p>

<h3>Примеры запросов</h3>

<pre><code># Получение токена
curl -X POST http://localhost:8000/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin", "password":"password123"}'

# Создание проекта (требуется роль editor)
curl -X POST http://localhost:8000/projects/ \
  -H "Authorization: Bearer {access_token}" \
  -H "Content-Type: application/json" \
  -d '{"title":"Новый жилой комплекс", "status":"active", "documents":[]}'

# Получение списка проектов
curl -X GET http://localhost:8000/projects/ \
  -H "Authorization: Bearer {access_token}"</code></pre>

<h2>📄 Лицензия</h2>
<p>MIT</p>
