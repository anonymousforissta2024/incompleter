#Source: https://stackoverflow.com/questions/75934628/typeerror-fastapi-sample-fails-during-loading
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}