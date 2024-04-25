# Simple CLI for library management system
def addBook(library):
    title = input("Enter the title of the book")
    author = input("Enter the author of the book")
    library[title]= author
    print("Your Book is successfully added to library")
    print(library)

def search(library):
    a = input("Enter the name of book")
    if a in library :
        print(f"{a} found with author {library[a]}")

def delete(library):
    a = input("Enter the book to be deleted")
    if a in library:
        del library[a]
        print("Book deleted successfully")
        print(library)

def main():
    library = {
        "Python xyz": "author1",
        "Python abc": "author2",
        "Java abc": "author3",
        "Java xyz": "author4"
    }

    print("Enter 1 for deletion")
    print("Enter 2 to add ")
    print("Enter 3 to search")

    action = int(input("Enter your choice"))
    if action==1:
        delete(library)
    elif action == 2:
        addBook(library)
    elif action == 3 :
        search(library)
    else:
        print("Invalid number")    


if __name__ == "__main__":
    main()        
