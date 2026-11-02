
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="DevOps Task API")

# Serve frontend CSS and JavaScript files
app.mount("/static", StaticFiles(directory="app/static"), name="static")


class Task(BaseModel):
    title: str
    completed: bool = False


tasks = [
    {"id": 1, "title": "Learn Python", "completed": True},
    {"id": 2, "title": "Build FastAPI application", "completed": False},
    {"id": 3, "title": "Learn Docker", "completed": False},
]


# Display the TaskFlow frontend
@app.get("/")
def root():
    return FileResponse("app/static/index.html")


# Health check endpoint for monitoring
@app.get("/health")
def health_check():
    return {"status": "healthy"}


# Retrieve all tasks
@app.get("/tasks")
def get_tasks():
    return tasks


# Retrieve a specific task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


# Create a new task
@app.post("/tasks")
def create_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": task.completed,
    }

    tasks.append(new_task)

    return new_task
