'''
Learned Installing FastAPI, Importing and creating Instance for FastAPI, Basic routing.
'''
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'data':'This is Home page'}

@app.get('/about')
def about():
    return {'data':'this is about page'}

