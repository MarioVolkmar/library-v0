from books import search_book_by_id, update_book_availability
from users import search_user_by_id

def borrow_book(books, users, loans, book_id, user_id):
    busq_b = search_book_by_id(books, book_id)
    busq_u = search_user_by_id(users, user_id)
    if busq_b is None:
        print("No existe el libro")
        return 
    if busq_u is None:
        print("No existe el usuario")
        return 
    if  busq_b["available"]:
        if len(loans) == 0:
            id_loan = 1
        else:
            id_loan = loans[0]["id_loan"]
            for l in loans:
                if l["id_loan"] >= id_loan:
                    id_loan = l["id_loan"] + 1
        loan = {
            "id_loan" : id_loan,
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
    busq = search_book_by_id(books, book_id) 
    if busq is not None and not busq["available"]:
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