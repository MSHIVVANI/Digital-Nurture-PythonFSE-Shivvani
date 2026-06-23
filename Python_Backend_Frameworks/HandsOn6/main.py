from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "FastAPI Running"
    }

@app.get("/courses")
def courses():
    return [
        {"id": 1, "name": "DBMS"},
        {"id": 2, "name": "Python"}
    ]