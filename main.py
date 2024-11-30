from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
@app.get("/hello/{item_id}")
async def hello(item_id: int):
    return {"item":item_id}

"""----------Lesson 3: Querry Parameters-------------"""
fake_db = [{"item_name":"Food"}, {"item_name":"Drink"},{"item_name":"Vegetable"}]
@app.get("/items")
async def list_items(skip: int = 0, total: int = 10):
    return fake_db[skip: skip + total]

@app.get("/admin/{name_admin}")
async def get_admin(name_admin: str, age: int | None = None, isNone : bool = True):
    admin = {"name":name_admin+ "is this page's admin"}
    if age:
        admin.update({"age":age})
    if isNone:
        admin.update({"level": "Admin of this page is setting already"})
    return admin 

"""-----------Lesson 4: Request Body-------------"""
class Shop_Item(BaseModel):
    name: str
    price : float 
    tax: float |None = None # Optional choice
    
@app.post("/shop")
async def shopping(item : Shop_Item):
    return item

@app.post("/total_shop")
async def total_shopping(item: Shop_Item):
    item_dict = item.dict()
    if item.tax:
        sum = item.tax + item.price
        item_dict.update({"Total": sum})
        return item_dict
    else:
        return item
    
@app.put("/put_route/{item_id}")
async def process_put(item_id: int, item : Shop_Item, q : bool |None = None):
    item_dict = item.dict()
    if q:
        item_dict.update({"Id of this item": item_id})
    return item_dict