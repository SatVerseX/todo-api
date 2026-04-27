from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app=FastAPI(title="Todo API",version="1.0.0")

todos=[]
counter={"id":1}

class Todo(BaseModel):
    title:str
    description:Optional[str]=None

class TodoUpdate(BaseModel):
    title:Optional[str]=None
    description:Optional[str]=None
    completed:Optional[bool]=None

@app.get("/")
def root():
    return {"message":"Welcome to Todo API"}        

@app.post("/todos",status_code=201)
def create_todo(todo:Todo):
    new_todo={
        "id":counter["id"],
        "title":todo.title,
        "description": todo.description,
        "completed": False,
        "created_at": str(datetime.now())
    }
    todos.append(new_todo)
    counter["id"]+=1
    return new_todo
@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo["id"]==todo_id:
            return todo
    return {"error":"Todo not found"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,update:TodoUpdate):
    for todo in todos:
        if todo["id"]==todo_id:
            if update.title: todo["title"]=update.title
            if update.description: todo["description"]=update.description
            if update.completed is not None: todo["completed"]=update.completed
            return todo
    return {"error":"Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for i,todo in enumerate(todos):
        if todo["id"]==todo_id:
            todos.pop(i)
            return {"message":"Todo deleted"}
    return {"error":"Todo not found"}        
    
