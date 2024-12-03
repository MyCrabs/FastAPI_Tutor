from fastapi import FastAPI, Query, Path, Form, Body
from pydantic import BaseModel

app = FastAPI()

@app.get("/get_items")
def get_itmes(q: str |None = Query(None, max_length=10, regex="fixedquery")):
    items = {"items": [{"item_id":"Coke"}, {"item_id":"Fanta"}]}
    if q:
        items.update({"q":q})
    return items

@app.get("/get_books")
def get_book(q :str |None =  Query(
    None, 
    min_length=3, 
    max_length=10,
    title = "This is title of query string",
    description="This is a simple query string",
    alias = "item-query")):
    books = {"book": [{"book_id":"Manga"}, {"book_title":"Conan"}]}
    if q:
        books.update({"q":q})
    return books
    
@app.get("/get_drinks")
def drink(q : list[str] = Query(["5","10"])):
    item = {"drink": [{"drink_id":"Coca"}, {"drink_price":"7000"}]}
    if q:
        item.update({"q":q})
    return item

"""-----------------Lesson 6: Path parameter and Numeric Validation--------------------"""

@app.get("/items_id/{id}")
async def read_items_id(
    id: int = Path(..., gt=5, lt=19),
    q: str = Query(None, max_length=10, alias="items_alias"),
    size: float = Query(..., gt=0, lt=6)
):
    result = {"items_id": id, "size": size}
    if q:
        result.update({"q": q})
    return result

"""-----------------Lesson 7: Body - multiple parameters------------------"""

class Item(BaseModel):
    name :str
    price : float
    description : str | None = None 
    
class User(BaseModel):
    username: str
    email: str
    full_name: str | None = None
    
@app.put("/items_put/{item_id}")
async def put_item(item_id : int = Path(..., gt=0, lt=10), 
                   q: str | None = None,
                   item_detail:Item | None = None,
                   user: User | None = None):
    item = {"item_id":item_id, "Item detail":item_detail, "user":user}
    if q:
        item.update({"q":q})
    return item

@app.post("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    result = {"item_id":item_id, "Item" : item}
    return result
    
class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/create-user/")
async def create_user(user: User):
    return {"message": f"User {user.name} created successfully"}

"""-----------------Lesson 8: Body - field------------------"""
@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"message": f"User {username} logged in"}