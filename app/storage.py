import json
import os

def load_data(file_path):
    if os.path.getsize(file_path) == 0:
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def save_data(file_path, data):
    with open(file_path, "w", encoding = "utf-8") as file:
        json.dump(data, file, indent = 4 , ensure_ascii=False)

    
def load_library_data():
    books = load_data("app/data_files/books.json")
    users = load_data("app/data_files/users.json")
    loans = load_data("app/data_files/loans.json")
    return books, users, loans

def save_library_data(books, users, loans):
    save_data("app/data_files/books.json", books)
    save_data("app/data_files/users.json", users)
    save_data("app/data_files/loans.json", loans)

