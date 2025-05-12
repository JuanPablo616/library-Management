import sys

# Lista de géneros válidos
VALID_GENRES = ["Fiction", "Non Fiction", "Science", "Biography", "Children"]

# Catálogo de libros
catalog = {}

def add_book(title, author, copies, genre):
    if genre not in VALID_GENRES:
        print(f"Error: '{genre}' is not a valid genre.")
        return
    if title in catalog:
        print(f"Book '{title}' already exists.")
        return
    catalog[title] = {
        'author': author,
        'copies': copies,
        'available': copies,
        'genre': genre
    }
    print(f"Book '{title}' added successfully.")

def search_book(title):
    book = catalog.get(title)
    if not book:
        print("Book not found.")
    else:
        print(f"Title: {title}\nAuthor: {book['author']}\nGenre: {book['genre']}\nAvailable: {book['available']}")

def loan_book(title):
    book = catalog.get(title)
    if not book:
        print("Book not found.")
        return
    if book['available'] == 0:
        print("No copies available for loan.")
        return
    book['available'] -= 1
    print(f"Book '{title}' loaned successfully.")

def return_book(title):
    book = catalog.get(title)
    if not book:
        print("Book not found.")
        return
    if book['available'] < book['copies']:
        book['available'] += 1
        print(f"Book '{title}' returned successfully.")
    else:
        print("All copies are already in the library.")

def delete_book(title):
    book = catalog.get(title)
    if not book:
        print("Book not found.")
        return
    if book['available'] == book['copies']:
        del catalog[title]
        print(f"Book '{title}' deleted successfully.")
    else:
        print("Cannot delete book with active loans.")

def list_books_by_genre(genre):
    if genre not in VALID_GENRES:
        print(f"'{genre}' is not a valid genre.")
        return
    found = False
    for title, book in catalog.items():
        if book['genre'] == genre:
            found = True
            print(f"Title: {title}, Author: {book['author']}, Available: {book['available']}")
    if not found:
        print(f"No books found for genre '{genre}'.")

def inventory_summary():
    total_titles = len(catalog)
    total_available = sum(book['available'] for book in catalog.values())
    print("--- Inventory Summary ---")
    print(f"Total book titles: {total_titles}")
    print(f"Total available copies: {total_available}")

# Puedes usar este bloque para pruebas rápidas
if __name__ == "__main__":
    add_book("1984", "George Orwell", 5, "Fiction")
    add_book("A Brief History of Time", "Stephen Hawking", 3, "Science")
    add_book("Steve Jobs", "Walter Isaacson", 2, "Biography")
    add_book("Green Eggs and Ham", "Dr. Seuss", 4, "Children")
    add_book("Sapiens", "Yuval Noah Harari", 6, "Non Fiction")

    search_book("1984")
    loan_book("1984")
    loan_book("1984")
    return_book("1984")
    delete_book("1984")
    list_books_by_genre("Fiction")
    inventory_summary()
