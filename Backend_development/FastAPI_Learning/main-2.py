'''
Path Parameters
'''

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'data':'home'}

@app.get('/blog/getallitems')
def getallitems():
    return {'data':{'item-1','item-2'}}

@app.get('/blog/{id}')
def blog(id: int):
    return {'data': id}



