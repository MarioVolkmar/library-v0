def add_book(books, title, author):
    busq = search_book_by_title(books, title)
    if len(books) == 0:
            id_book = 1
    else:
        id_book = books[0]["id_book"]
        for b in books:
            if b["id_book"] >= id_book:
                id_book = b["id_book"] + 1
                
    if len(busq) != 0:
        for b in busq:
            if b["author"].lower() == author.strip().lower():
                print("El libro ya se encuentra ingresado")
                return None
    book = {
        "id_book" : id_book,
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
    busq = search_book_by_id(books, book_id) 
    if busq is not None:
        busq["available"] = not busq["available"]
        return busq["available"]
    return None
    
def search_book_by_id(books, id):
    for b in books:
        if b["id_book"] == id:
            return b
    return None