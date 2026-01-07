from fastapi import FastAPI,status,UploadFile
from d_types import Color
from pydantic import BaseModel
from routers import user_router

class Item(BaseModel):
    name:str
    description:str=None
    price:float =None
    tax:float=None

class User(BaseModel):
    uname:str
    password:str
    email:str

class Resp(BaseModel):
    uname:str
    email:str


app=FastAPI()
app.include_router(user_router)

@app.post("/upload")
async def uploadf(file:UploadFile):
    fname=file.filename
    content= await file.read()
    return {"filename":fname,"content":content}

@app.post('/usr',response_model=Resp,status_code=status.HTTP_201_CREATED)
def create_user(user:User):
    return user


@app.get("/color/{color}")
def main(color:Color):
    return color

@app.post("/add")
def create_item(item:Item):
    itdct=item.model_dump()
    itdct.update({"location":"Kigali"})
    return {**itdct}

