# Fast API Notes

## Introduction
Fast API is a webframe work used to develop and built web applicationas and webisites without creating from the scratch

## Features
- Very Fast
- Easy to Learn
- In-built Documentation Support

## Path Parameters

Path parameters are like the variables we can declare them as like we declare in Python

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
 ```

The item_id will pass through the function as the argument item_id

We can declare the path parameter types in the function 