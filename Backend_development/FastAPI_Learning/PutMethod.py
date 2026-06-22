'''
Example for Request body and PUT method
'''

from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
student_details ={
    1: {
        'name':'Sumanth',
        'age':21,
        'Address': 'Newyork'
        },
    2: {
        'name':'Adam',
        'age':21,
        'Address': 'Chicago'
       },
    3: {
        'name':'Bob',
        'age':21,
        'Address': 'California'
       }
    }

class Student(BaseModel):
    name: str
    age: int
    Address: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    Address: Optional[str] = None

@app.get("/")
def index():
    return{'data':'Home page'}

'''Path Parameter'''
@app.get("/get-students/{student_id}")
def get_student(student_id: int = Path(..., description="Choose id to get student details", gt=0)):
    return student_details[student_id]

'''Query Parameter'''
@app.get('/get-student')
def get_student(*, name: Optional[str], Test: int = None):
    for st_id in student_details:
        if student_details[st_id]['name'] == name:
            return student_details[st_id]
    return {'result': 'Not Found'}

'''POST Method and Request Body'''
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in student_details:
        return {"Message":"Data already exists"}
    else:
        student_details[student_id] = student
        return student_details[student_id]
    

'''PUT Method and Request Body'''
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student : UpdateStudent):
    if student_id not in student_details:
        return {'Message': 'Data Not found'}
    else:
        if student.name != None:
            student_details[student_id].name = student.name
        
        if student.age != None:
            student_details[student_id].age = student.age

        if student.Address != None:
            student_details[student_id].Address = student.Address
        
        return student_details[student_id]