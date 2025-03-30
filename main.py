from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# 
data_store = []

# pydantic model for post request validation
class transaction(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    

@app.get('/')
def health():
    return {"message": "Server is running", "status": "200" }

@app.get('/getData')
async def read():
    try:
        return { 'message': 'Data retrieved successfully', "data": data_store }
    except Exception as error:
        return { 'error': str(error) }

@app.post('/insert')
async def insert(data:transaction):
    try:
        dictionay_data = data.model_dump() # if duplicate data comes it automatically filter out
        print('Dictionay data', dictionay_data)
        data_store.append(dictionay_data)
        return { 'message': 'Data inserted successfully', "data": data_store }
    except Exception as error:
        return { 'error': str(error) }