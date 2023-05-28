from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/api-endpoint")
async def first_api():
    return {"message": "Hello Eric!"}


@app.get("/books")
async def read_all_books():
    return BOOKS


# @app.get("/book/{book_title}")
# async def read_book(book_title: str):
#     return {"params": book_title}


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/book/{book_title}")
async def read_book_with_title(book_title: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold() and book.get("title").casefold() == book_title.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/book/author/{author}")
async def read_book_with_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create-book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return BOOKS


@app.put("/books/update-book")
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == update_book.get("title").casefold():
            BOOKS[i] = update_book
    return BOOKS


@app.delete("/books/delete-book")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
