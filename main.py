from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello from FastAPI on Render!</h1>"

@app.get("/ping")
async def ping():
    return {"message": "pong"}

