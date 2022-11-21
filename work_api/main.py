from fastapi import FastAPI
from routers import train

app = FastAPI()


@app.get("/")
async def root():
    return {"Welcom to our API": "This API deals with Train information."}

def config_router():
    app.include_router(train.router)

config_router()