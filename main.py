from fastapi import FastApI , HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastApI()

task = {}

class Tasks:
    todo = Optional[str] = None
    completed = Optional[bool] = None
class Updatedtask:
    todo = Optional[str] = None
    completed = Optional[bool] = None

@app.post("/tasks/{task_id}")
def create_task(task_id: int, task: task):
    if task_id in task:
        raise HTTPException(status_code=400, detail= "Task Already Exists")
    tasks[task_id] = task.dict()
    return {"Text":"Task created Suscessfully"}

@app.get("/tasks/{task_id}")
def fetch(task_id : int):
    if task_id not in task:
        raise HTTPException(status_code=404, detail = "Task Not found")
    return tasks[task_id]

@app.put("/tasks/{task_id}")
def change(task_id : int, task:Updatedtask):
    if task_id not in task:
        raise HTTPException(status_code=404 , detail= "Task not found")
    
    tasks[task_id] = task.dict()
    return {"Text":"Task changed Suscessfully"}
        
@app.patch("/tasks/{task_id}")
def patching(task_id: int, patch_task : Updatedtask):
    if task_id not in task:
        raise HTTPException(status_code=400, detail= "Task not Found")
    
    current_task = tasks[task_id]

    if patch_task in not None:
        current_task['todo'] = patch_task.todo
    if patch_task.completed is not None:
        current_task['completed'] = patch_task.completed

    return {"Text": "Task Edited Suscessfully"}
