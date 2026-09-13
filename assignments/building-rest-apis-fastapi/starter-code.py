from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


tasks: list[Task] = []


@app.get("/")
def read_root():
    """Return a welcome message for the API."""
    pass


@app.get("/health")
def health_check():
    """Report whether the API is running."""
    pass


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    """Return all tasks."""
    pass


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    """Create and return a task."""
    pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    """Return one task or a 404 error."""
    pass


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskCreate):
    """Replace an existing task or return a 404 error."""
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    """Delete a task or return a 404 error."""
    pass
