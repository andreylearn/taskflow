# TaskFlow

Учебный DevOps-проект: REST API для управления задачами.

Цель проекта — на практике пройти путь от простого приложения с базой данных до контейнеризации, CI/CD и развёртывания в Kubernetes.

## Текущий стек

- Python 3
- FastAPI
- PostgreSQL 16
- SQLAlchemy
- Docker и Docker Compose
- Git и GitHub

## Архитектура

```text
Клиент
  ↓ HTTP
FastAPI
  ↓ SQL
PostgreSQL
FastAPI и PostgreSQL работают в отдельных Docker-контейнерах. Данные базы хранятся в Docker volume, поэтому сохраняются между перезапусками контейнеров.
Возможности API
Проверка состояния сервиса.
Получение списка задач.
Создание новой задачи.
Хранение задач и пользователей в PostgreSQL.
Структура проекта
taskflow/
├── app/
│   └── main.py              # FastAPI-приложение
├── db/
│   └── 001_init.sql         # Первая SQL-миграция
├── Dockerfile               # Образ API
├── docker-compose.yml       # Локальный запуск API и PostgreSQL
├── requirements.txt         # Python-зависимости
└── README.md
Быстрый запуск
Нужен установленный Docker Desktop.
Запустить API и PostgreSQL:
docker compose up --build -d
Проверить контейнеры:
docker compose ps
Остановить сервисы:
docker compose down
Инициализация новой базы
При первом запуске на новом компьютере нужно применить SQL-миграцию:
docker compose exec -T db psql -U taskflow -d taskflow < db/001_init.sql
Проверка API
Проверка состояния:
curl http://127.0.0.1:8000/health
Ожидаемый ответ:
{
  "status": "ok"
}
Получить список задач:
curl http://127.0.0.1:8000/tasks
Swagger-документация FastAPI:
http://127.0.0.1:8000/docs
API-методы
Метод	Путь	Назначение
GET	/health	Проверка работоспособности API
GET	/tasks	Получение списка задач
POST	/tasks	Создание задачи


Пример создания задачи:
{
  "user_id": 1,
  "title": "Настроить GitHub Actions",
  "status": "todo",
  "priority": 2
}
SQL-практика
В проекте используются:
таблицы users и tasks;
внешний ключ tasks.user_id → users.id;
JOIN для получения задач вместе с email пользователя;
индекс idx_tasks_user_status по user_id и status;
ограничения статуса и приоритета задач;
SQL-миграция для создания схемы.
Дальнейший план

Создать FastAPI и PostgreSQL.

Написать SQL-миграцию.

Добавить Docker Compose.

Собрать API в Docker-образ.

Опубликовать код на GitHub.

Добавить автоматическое применение миграций.

Написать тесты API.

Настроить GitHub Actions: тесты и сборка образа.

Опубликовать Docker-образ в GitHub Container Registry.

Развернуть сервис в Kubernetes.

Упаковать Kubernetes-манифесты в Helm chart.

Автоматизировать подготовку VM через Ansible.

Добавить мониторинг с Prometheus и Grafana.