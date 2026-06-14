from books import search_book_by_id, update_book_availability
from users import search_user_by_id

def borrow_book(books, users, loans, book_id, user_id):
    if search_book_by_id(books, book_id) is None:
        print("No existe el libro")
        return 
    if search_user_by_id(users, user_id) is None:
        print("No existe el usuario")
        return 
    if  search_book_by_id(books, book_id)["available"]:
        id = len(loans) + 1
        loan = {
            "id_loan" : int(id),
            "book_id" : book_id,
            "user_id" : user_id,
            "active" : True
        }
        loans.append(loan)
        update_book_availability(books, book_id)
        print("Prestamo Exitoso")
        return 
    print("El libro ya se encuentra prestado")
    return None
    
def return_book(books, loans, book_id):
    if search_book_by_id(books, book_id) is not None and not search_book_by_id(books, book_id)["available"]:
        for loan in loans:
            if loan["active"] and loan["book_id"] == book_id:
                loan["active"] = False
                update_book_availability(books, book_id)
                print("Devolucion exitosa")
                return  
        return None
    return None
        

def list_loans(loans):
    return loans