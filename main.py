from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class User(BaseModel):
    id: int
    name: str
    
@app.post("/home")
async def home(user: User):
    return {"message":"User be created successfully", "user":user}
