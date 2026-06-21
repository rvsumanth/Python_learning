'''Example code for demonstrating path parameters'''


from fastapi import FastAPI, Path

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

'''Single path parameter'''
@app.get("/get-students/{student_id}")
def get_student(student_id: int = Path(..., description="Choose id to get student details", gt=0, le=3)):
    return students[student_id]

'''Multiple path parameter example'''

@app.get('/item/{item_id}/order/{order_id}')
def item_orders(item_id: int, order_id: int):
    return {
        'item id': item_id,
        'order id': order_id
    }
