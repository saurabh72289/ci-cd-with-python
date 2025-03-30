from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def get_root():
    return {"message":"this id CI/CD from backend !!!!"}