from fastapi import FastAPI
from app.api.routes import router as UserRouter

app = FastAPI()

app.include_router(UserRouter,prefix="/api")

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run("main:app",host="127.0.0.1",port=5000,reload=True)