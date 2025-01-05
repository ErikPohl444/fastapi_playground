from typing import Union
import requests
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hipstercount/")
def read_item(q: Union[str, None] = None):
    res = requests.get("http://hipsum.co/api/?type=hipster-centric&sentences=3")
    return {"Yo": res.content.decode()}


'''
    print(res)
    return {"sample": res, "q": q}
'''
