from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def greet():
    return {"Hello World"}

@app.get("/user/{name}")
def greet_user(name):
    return {f"Hello {name}"}