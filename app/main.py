import os
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://taskflow:taskflow_dev_password@localhost:5432/taskflow",
)

engine = create_engine(DATABASE_URL)

app = FastAPI(title="TaskFlow API")


class TaskCreate(BaseModel):
    user_id: int
    title: str
    status: str = "todo"
    priority: int = 3


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks():
    query = text("""
        SELECT
            tasks.id,
            tasks.title,
            tasks.status,
            tasks.priority,
            users.email
        FROM tasks
        JOIN users ON users.id = tasks.user_id
        ORDER BY tasks.id;
    """)

    with engine.connect() as connection:
        rows = connection.execute(query).mappings().all()

    return [dict(row) for row in rows]


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    query = text("""
        INSERT INTO tasks (user_id, title, status, priority)
        VALUES (:user_id, :title, :status, :priority)
        RETURNING id, title, status, priority;
    """)

    with engine.begin() as connection:
        row = connection.execute(
            query,
            {
                "user_id": task.user_id,
                "title": task.title,
                "status": task.status,
                "priority": task.priority,
            },
        ).mappings().one()

    return dict(row)