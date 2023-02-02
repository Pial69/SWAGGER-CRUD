
import shutil
from typing import List
from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post("/")
def root(file: UploadFile = File(...)):
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return{"file_name": file.filename}

@app.post("/img")
def upload_image(files: List[UploadFile]= File(...)):
    for img in files:
        with open(f'{img.filename}', "wb") as buffer:
            shutil.copyfileobj(img.file, buffer)

    return {"file_name": "RESPONSIVE"}





#db ={}
"""
#from pydantic import BaseModel


class Item(BaseModel):
    name: str
    desc: str
@app.post("/")
def create(item: Item): 
    db[item.name] = item.desc
    return {"item": item}


@app.get("/")
def get_all_data():
    return db


@app.delete("/")
def delete_data(name: str):
    del db[name]
    return db

@app.put("/")
def update_data(item: Item): 
    db[item.name] = item.desc
    return {"item": item}

"""