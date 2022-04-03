from fastapi import FastAPI
import models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def read_all():
    return {"Database":"Created"}
