from utils import database
SYSTEM_RESPONSES = lambda attribute: (f"Enter the new book {attribute}:\t")
USER_CHOICE= """
Enter:
-'a' to add a new book
-'l' to list all books
-'r' to mark a book as read
-'d' to delete a book
-'q' to quit

Your choice: """

def menu():
    database.create_book_table()
    user_input=input(USER_CHOICE)
    while user_input!='q':
        if user_input=='a':
            prompt_add_book()

        elif user_input=='l':
            list_books()
        elif user_input=='r':
            prompt_read_book()
        elif user_input=='d':
            prompt_delete_book()
        
        user_input=input(USER_CHOICE)
def prompt_add_book():
    name=input(SYSTEM_RESPONSES("name"))
    author=input(SYSTEM_RESPONSES("author"))
    database.insert_book(name,author)

def prompt_read_book():
    name=input("Enter the name of the book you just fineshed reading: ")
    
    database.mark_book_as_read(name)

def list_books():
    for book in database.get_all_books():
        read='YES' if book[3]==1 else 'NO' #modify the True->YES and False into NO
        print(f"{book[1]} by {book[2]} -Read: {read}") #print information
def prompt_delete_book():
    
    name=input("Enter the name of the book you just fineshed reading: ")
    database.delete_book(name)



menu()