# FastAPI CRUD - Student API

A simple FastAPI project for managing students with CRUD operations.

## Features
- Create, Read, Update, Delete students
- Path and query parameter validation
- Pydantic models
- Swagger UI documentation

## Installation
```bash
git clone https://github.com/your-username/fastapi-crud.git
cd fastApiCRUD
python -m venv venv
# Activate venv:
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
pip install fastapi uvicorn pydantic
Run
bash
Copier le code
uvicorn main.main:app --reload
API: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

Endpoints
Method	Endpoint	Description
GET	/	Welcome message
GET	/get-all-students	Get all students
GET	/get-student/{student_id}	Get student by ID
GET	/get-by-name	Get student by name/age
POST	/create-student/{student_id}	Create student
PUT	/update-student/{student_id}	Update student
DELETE	/delete-student/{student_id}	Delete student

License
MIT

vbnet
Copier le code

This is **short, professional, and complete** for GitHub.  

I can also make an **even shorter one-liner version** that’s ultra-compact if you want. Do you want me to do that?






