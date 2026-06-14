from books import search_book_by_id, update_book_availability
from users import search_user_by_id

def borrow_book(books, users, loans, book_id, user_id):
    if search_book_by_id(books, book_id) == None:
        return "No existe el libro"
    if search_user_by_id(users, user_id) == None:
        return ("No existe el usuario",search_user_by_id(users, user_id))
    if  search_book_by_id(books, book_id)["available"]:
        id = len(loans) + 1
        loan = {
            "id" : int(id),
            "book_id" : book_id,
            "user_id" : user_id,
            "active" : True
        }
        loans.append(loan)
        update_book_availability(books, book_id, False)
        return "Prestamo Exitoso"
    return None
    
def return_book(books, loans, book_id):
    if search_book_by_id(books, book_id) != None and not search_book_by_id(books, book_id)["available"]:
        for loan in loans:
            if loan["active"] and loan["book_id"] == book_id:
                loan["active"] = False
                update_book_availability(books, book_id, True)
                return "Devolucion exitosa" 
        return None
    return None
        

def list_loans(loans):
    return loans