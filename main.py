from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI()

class Book(BaseModel):
    id:int
    name:str
    pages:int

books:List[Book]=[]

@app.get("/")
def mainHomePage():
    return {"message":"Hi this is root Home Page message that you just got from the server/database/ram"}

@app.get("/books")
def getAllBooks():
    return books

@app.post("/books")
def addBook(incomingBook:Book):
    books.append(incomingBook)
    return {"message":"book added"}

@app.put("/books/{book_id}")
def updateExistingBook(book_id:int,updatedBook:Book):
    for index,book in enumerate(books):
        if(book.id==book_id):
            books[index]=updatedBook
            return {"message":"Book Updated"}
    return {"error":"stated book_id not found"}

@app.delete("/books/{book_id}")
def deleteBook(book_id:int):
    for index,book in enumerate(books):
        if book.id==book_id:
            books.pop(index)
            return {"message":"book deleted"}
        
    return {"error":"stated bookid not found"}
        



