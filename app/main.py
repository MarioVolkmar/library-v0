from data import books, users, loans
from books import add_book, list_books, search_book_by_title
from users import add_user, list_users, search_user_by_email
from loans import borrow_book, return_book, list_loans

add_book(books, "Clean Code", "Robert C. Martin")
add_book(books, "Python Crash Course", "Eric Matthes")
add_book(books, "Python Crash Course", "Mario Volkmar")
add_book(books, "Clean Code", "Robert C. Martin")
print(list_books(books))

add_user(users, "Mario", "mario@email.com")
add_user(users, "Mario", "mario@email.com")
add_user(users, "Alejo", "alejo@email.com")
print(list_users(users))

print(borrow_book(books, users, loans, 2, 1))
print(borrow_book(books, users, loans, 2, 1))
print(borrow_book(books, users, loans, 3, 2))
print(list_loans(loans))
print(list_books(books))

print(return_book(books, loans, 2))
print(list_loans(loans))
print(list_books(books))