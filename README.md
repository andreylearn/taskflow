# TaskFlow

Учебный DevOps-проект: REST API для управления задачами.

## Стек

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker и Docker Compose
- Git и GitHub

## Архитектура

```text
Клиент → FastAPI → PostgreSQL
```

API и PostgreSQL работают в отдельных Docker-контейнерах. Данные базы сохраняются в Docker volume между перезапусками.

## Структура проекта

```text
taskflow/
├── app/
│   └── main.py
├── db/
│   └── 001_init.sql
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Запуск

Нужен установленный Docker Desktop.

```bash
docker compose up --build -d
```

Проверить контейнеры:

```bash
docker compose ps
```

Остановить сервисы:

```bash
docker compose down
```

## Инициализация базы данных

При первом запуске на новой машине примени миграцию:

```bash
docker compose exec -T db psql -U taskflow -d taskflow < db/001_init.sql
```

## Проверка API

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/tasks
```

Swagger-документация: `http://127.0.0.1:8000/docs`

## API

| Метод | Путь | Назначение |
|---|---|---|
| `GET` | `/health` | Проверка работоспособности API |
| `GET` | `/tasks` | Получение списка задач |
| `POST` | `/tasks` | Создание задачи |

Пример запроса для создания задачи:

```json
{
  "user_id": 1,
  "title": "Настроить GitHub Actions",
  "status": "todo",
  "priority": 2
}
```

## SQL-практика

- Таблицы `users` и `tasks`.
- Внешний ключ между задачей и пользователем.
- `JOIN` для получения задач с email пользователя.
- Индекс по `user_id` и `status`.
- Ограничения на статус и приоритет.
- SQL-миграция для создания схемы базы.

## План развития

- [x] FastAPI и PostgreSQL
- [x] SQL-миграция
- [x] Docker Compose
- [x] Docker-образ API
- [x] GitHub-репозиторий
- [ ] Автоматические миграции
- [ ] Тесты API
- [ ] GitHub Actions
- [ ] Публикация Docker-образа
- [ ] Kubernetes и Helm
- [ ] Ansible для подготовки VM
- [ ] Prometheus и Grafana