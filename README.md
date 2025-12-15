# FastAPI CRUD - Student API

A simple FastAPI project for managing students with CRUD operations.

## Features
- Create, Read, Update, Delete students
- Path and query parameter validation
- Pydantic models
- Swagger UI documentation

## Installation & Run
pip install fastapi uvicorn pydantic  
uvicorn main.main:app --reload  
API: http://127.0.0.1:8000 | Swagger UI: http://127.0.0.1:8000/docs

## Endpoints
GET    /            Welcome message   
GET    /get-all-students  Get all students  
GET    /get-student/{student_id}  Get student by ID  
GET    /get-by-name  Get student by name/age  
POST   /create-student/{student_id}  Create student  
PUT    /update-student/{student_id}  Update student  
DELETE /delete-student/{student_id}  Delete student  

## License
MIT

                                                      Realized by Wassim Hamdi

