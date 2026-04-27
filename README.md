# Todo API 🚀

A REST API built with Python and FastAPI.

## Features
- Create, Read, Update, Delete tasks
- Auto-generated Swagger documentation
- Input validation with Pydantic
- Timestamp on every task

## Tech Stack
- Python 3.10
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. Clone the repo
   git clone https://github.com/SatVerseX/todo-api.git
   cd todo-api

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run the server
   uvicorn main:app --reload

## API Endpoints

| Method | Endpoint      | Description        |
|--------|-------------- |--------------------|
| GET    | /             | Welcome message    |
| POST   | /todos        | Create a task      |
| GET    | /todos        | Get all tasks      |
| GET    | /todos/{id}   | Get single task    |
| PUT    | /todos/{id}   | Update a task      |
| DELETE | /todos/{id}   | Delete a task      |

## API Docs
Run the server and visit:
http://127.0.0.1:8000/docs