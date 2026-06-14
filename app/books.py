def add_book(books, title, author):
    if search_book_by_title(books, title) == None:
        id = len(books) + 1
        book = {
            "id" : int(id),
            "title" : title,
            "author" : author,
            "available" : True
        }
        books.append(book)
        return
    else:
        if search_book_by_title(books, title)["author"] == author:
            return None
        id = len(books) + 1
        book = {
            "id" : int(id),
            "title" : title,
            "author" : author,
            "available" : True
        }
        books.append(book)
        return


def search_book_by_title(books, title):
    for b in books:
        if b["title"].lower() == title.strip().lower():
            return b
    return None
    
def list_books(books):
    return books

def update_book_availability(books, book_id, available):
    for b in books: 
        if b["id"] == book_id:
            b["available"] = available
            return 
    return None
    
def search_book_by_id(books, id):
    for b in books:
        if b["id"] == id:
            return b
    return None