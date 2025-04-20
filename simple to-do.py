from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Task(BaseModel):
    id : int
    name : str
    description: str
    

tasks : list[Task] = []

@app.post("/create-task")
def create_task(task: Task):
    tasks.append(task)
    return {f"Task {task.name} has been created with ID : {task.id}!"}

@app.get("/get-tasks")
def get_tasks():
    return tasks

@app.get("/get-task")
def get_task(id : int):
    for task in tasks:
        if task.id == id:
            return task
    return {f"There is no task with id {id}"}
