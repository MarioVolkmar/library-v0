def add_book(books, title, author):
    if len(search_book_by_title(books, title)) == 0:
        id = len(books) + 1
        book = {
            "id_book" : int(id),
            "title" : title,
            "author" : author,
            "available" : True
        }
        books.append(book)
        print("Libro ingresado")
        return
    else:
        for b in search_book_by_title(books, title):
            if b["author"].lower() == author.strip().lower():
                print("El libro ya se encuentra ingresado")
                return None
        id = len(books) + 1
        book = {
            "id_book" : int(id),
            "title" : title,
            "author" : author,
            "available" : True
        }
        books.append(book)
        print("Libro ingresado")
        return


def search_book_by_title(books, title):
    res = []
    for b in books:
        if b["title"].lower() == title.strip().lower():
            res.append(b)
    return res
    
def list_books(books):
    return books

def update_book_availability(books, book_id):
    if search_book_by_id(books, book_id) is not None:
        search_book_by_id(books, book_id)["available"] = not search_book_by_id(books, book_id)["available"]
        return search_book_by_id(books, book_id)["available"]
    return None
    
def search_book_by_id(books, id):
    for b in books:
        if b["id_book"] == id:
            return b
    return None