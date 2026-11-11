from fastapi import FastAPI
from schemas.auth_schemas import UserCreate

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Welcome to the Dev Circle Backend!"}


@app.post("/auth/registration")
def create_new_user_handler(payload:UserCreate):
    print(payload)
    return {"message":"User created successfully!"}