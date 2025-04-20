from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def greet():
    return {"greeting":"Hello World"}

@app.get("/user/{name}")
def greet_user(name : str):
    return {"greeting":f"Hello {name}"}

@app.get("/welcome")
def greet_with_age(name : str = "user", age : int = 69):
    return {"greeting":f"Hello {name}",
            "age": age
        }

if __name__=="__main__":
    import uvicorn
    uvicorn.run("basics:app", host="127.0.0.1", port=8001, reload=True)