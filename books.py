from fastapi import FastAPI
from enum import Enum
app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'},
}

class DirectionName (str, Enum):
    north = "North"
    south = "South"
    east  = "East"
    west  = "West"

@app.get("/")
async def read_all_books():
    return BOOKS

@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if (direction_name == DirectionName.north):
        return {"Direction": direction_name, "sub": "Up"}
    if (direction_name == DirectionName.south):
        return {"Direction": direction_name, "sub": "Down"}
    if (direction_name == DirectionName.east):
        return {"Direction": direction_name, "sub": "Right"}
    return {"Direction": direction_name, "sub": "Left"}


@app.get("/books/mybook")
async def read_favorite_book():
    return {"book_title":"My Favorite Book"}

@app.get("/books/{book_name}")
async def read_book(book_name:str):
    return BOOKS[book_name]

