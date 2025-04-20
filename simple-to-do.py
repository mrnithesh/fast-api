from fastapi import FastAPI, HTTPException
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

@app.get("/get-task/{id}")
def get_task(id : int):
    for task in tasks:
        if task.id == id:
            return task
    raise HTTPException (status_code=404, detail="There is no task found")

@app.put("/update-task/{id}")
def update_task(id: int, updated_task : Task):
    for i, task in enumerate(tasks):
        if task.id == id:
            tasks[i]=updated_task
            return {f"The task {id} is updated successfully!"}
    raise HTTPException(status_code=404, detail="There is no task found")

@app.delete("/delete-task/{id}")
def delete_task(id: int):
    for i, task in enumerate(tasks):
        if task.id==id:
            tasks.pop(i)
            return {f"The task with id {id} has been deleted successfully!"}
    raise HTTPException(status_code=404, detail="No task found!")
