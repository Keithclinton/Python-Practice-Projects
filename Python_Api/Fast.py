from fastapi import FastAPI
apps = FastAPI()
@apps.get("/")
def home():
    return {"Data": "Test"}
@apps.get("/about")
def about():
    return{"Data: About"}


inventory = {
    1: {
        "name": "Milk",
        "Price": 55,
        "Brand": "Regular"
    }
}
@apps.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description= "The id of the item")):
    return inventory[item_id]
