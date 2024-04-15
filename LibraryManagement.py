# Simple CLI for library management system

def addBook():
    title = input("Enter the title of the book")
    author = input("Enter the author of the book")
    library[title]= author
    print("Your Book is successfully added to library")
    print(library)

def main():
    library = {
        "python xyz": "author1",
        "Python abc": "author2",
        "Java abc": "author3",
        "Java xyz": "author4"
    }

    search = input("Enter the title of the book to search: ")

    # Use the get() method to search for the book title in the library dictionary
    book = library.get(search)

    if book:
        print(f"Book found!\nTitle: {search}\nAuthor: {book}")
    else:
        print("Book not found in the library.")
