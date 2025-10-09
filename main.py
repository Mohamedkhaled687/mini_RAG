from fastapi import FastAPI


app = FastAPI()


@app.get("/welcome")
def welcome():
    return {"message": "Hello, mini_RAG!"}

