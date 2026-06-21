from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()
students ={
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

@app.get("/")
def index():
    return{'data':'Home page'}

'''Path Parameter'''
@app.get("/get-students/{student_id}")
def get_student(student_id: int = Path(..., description="Choose id to get student details", gt=0, le=3)):
    return students[student_id]

'''Query Parameter'''
@app.get('/get-student')
def get_student(*, name: Optional[str], Test: int = None):
    for st_id in students:
        if students[st_id]['name'] == name:
            return students[st_id]
    return {'result': 'Not Found'}
