import shutil
from typing import List
from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post("/")
async def root(file: UploadFile = File(...)):
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_name": file.filename}


@app.post("/img")
async def upload_image(files: List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}', "wb") as buffer:
            shutil.copyfileobj(img.file, buffer)

    return {"file_name": "Good"}
