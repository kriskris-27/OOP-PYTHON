from fastapi import FastAPI

from app.routers import health

app = FastAPI(
    title="My API",
    version="0.1.0",
)

app.include_router(health.router)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}
