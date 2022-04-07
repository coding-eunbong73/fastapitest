from fastapi import FastAPI, Depends, HTTPException
import models
from database import engine, SessionLocal
from routers import auth, todos
from companyapis import companyapis

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(
    companyapis.router,
    prefix="/companyapis",
    tags=["companyapis"],
    responses={418: {"description": "Internal Use Only"}}
)
