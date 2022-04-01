from typing import Optional

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
async def read_all_books(default_book: str = "book_3", skip_optional_book: Optional[str] = None):
    if skip_optional_book:
        new_books = BOOKS.copy()
        del new_books[skip_optional_book]
        return new_books
    return BOOKS

@app.get("/test2")
async def read_all_books_required( skip_book: str ):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
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

