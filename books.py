from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def first_api():
    return {"message": "hello EunBong"}
