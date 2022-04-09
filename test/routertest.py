from fastapi import FastAPI, Depends, HTTPException
from companyapis import companyapis, dependencies

app = FastAPI()

app.include_router(
    companyapis.router,
    prefix="/companyapis",
    tags=["companyapis"],
    dependencies=[Depends (dependencies.get_token_header)],
    responses={418: {"description": "Internal Use Only"}}
)
