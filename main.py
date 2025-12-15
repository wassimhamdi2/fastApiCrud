from fastapi import FastAPI, Path, Query
from typing import Optional, Dict
from pydantic import BaseModel


app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None



students: Dict[int, Student] = {
    1: Student(name="John", age=17, year="Year 12"),
    2: Student(name="Jane", age=16, year="Year 11"),
    3: Student(name="Alex", age=18, year="Year 13")
}

@app.get("/")
def index():
    return {"message": "Welcome to the Student API!"}




@app.get("/get-all-students")
def get_all_students():
    if len(students) == 0:
        return {"Error": "There are no students"}
    return students

    



@app.get("/get-student/{student_id}")
def get_student(
    student_id: int = Path(..., gt=0)
):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    return students[student_id]




@app.get("/get-by-name")
def get_student_by_name(
    name: Optional[str] = None, 
    age: Optional[int] = Query(None, gt=15)
):
    for student_id in students:
        student = students[student_id]
        
        name_match = name is None or student.name == name
        age_match = age is None or student.age == age

        if name_match and age_match:
            return student
            
    return {"Error": "Data not found"}




@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student ID already exists"}
    
    students[student_id] = student
    return students[student_id]




@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    existing_student = students[student_id]

    if student.name is not None:
        existing_student.name = student.name
    if student.age is not None:
        existing_student.age = student.age
    if student.year is not None:
        existing_student.year = student.year

    return existing_student




@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    del students[student_id]
    return {"message": "Student deleted successfully"}