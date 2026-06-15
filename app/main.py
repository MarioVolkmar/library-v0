## from data import books, users, loans
from books import add_book, list_books
from users import add_user, list_users
from loans import borrow_book, return_book, list_loans
from storage import load_library_data, save_library_data



books, users, loans = load_library_data()

print(books)
print(users)
print(loans)

add_book(books, "Clean Code", "Robert C. Martin")
add_book(books, "Python Crash Course", "Eric Matthes")
add_book(books, "Python Crash Course", "Mario Volkmar")
add_book(books, "Clean Code", "Robert C. Martin")
print(list_books(books))

add_user(users, "Mario", "mario@email.com")
add_user(users, "Mario", "mario@email.com")
add_user(users, "Alejo", "alejo@email.com")
print(list_users(users))

borrow_book(books, users, loans, 2, 1)
borrow_book(books, users, loans, 2, 1)
borrow_book(books, users, loans, 1, 2)
print(list_loans(loans))
print(list_books(books))

return_book(books, loans, 2)
print(list_loans(loans))
print(list_books(books))

save_library_data(books, users, loans)