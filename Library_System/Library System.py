# Malak Ahmed Samih
#------------------------------------Library Operations Class--------------------------------------------#
class library:
    def __init__(self, name, booklist):
        self.name = name
        self.booklist = [book.lower() for book in booklist]
        self.lendedbooks = {}

    def displaybooks(self):
        print(f"\nWe have following books in {self.name} library:")
        if not self.booklist:
            print("\nNo books available")
        else:
           for i, book in enumerate(self.booklist, start=1):
                print(f"{i}. {book.capitalize()}")
 

    def lendbook(self, user, book):
        if book in self.booklist:
            self.lendedbooks[user] = book
            self.booklist.remove(book)
            print(f"\nHello {user} . You can keep The {book.capitalize()} book for 30 days")
        elif book in self.lendedbooks.values():
            print(f"\nThe book {book.capitalize()} is already lended out")   
        else: 
            print("\nWe don't have this book in our library")

    def addbook(self, book):
        self.booklist.append(book)
        print(f"\nThe {book.capitalize()} book has been added to the library")     

    def returnbook(self, user):
        if user in self.lendedbooks:
            self.booklist.append(self.lendedbooks[user])
            del self.lendedbooks[user]
            print(f"\nThanks {user.capitalize()} for returning the book")
        else:
            print("\nYou didn't lend any book from us")

    def show_lendedbooks(self):
        if not self.lendedbooks:
            print("\nNo books are currently lended out")
        else:
            print("\nLended Books:")
            for user, book in self.lendedbooks.items():
                print(f"{user.capitalize()} has borrowed {book.capitalize()}")                   

#------------------------------------The Main---------------------------------------------#

Harry = library("CodeWithHarry", ['Python', 'Rich Dad Poor Dad', 'C++', 'Java', 'Data Science', 'Machine Learning', 'Algorithms by CLRS'])
print("______Welcome to the CodeWithHarry Library______")
while True:
    print("Enter your choice to continue: ")
    print("     1. Display Books")
    print("     2. Lend a Book")
    print("     3. Add a Book")
    print("     4. Return a Book")
    print("     5. Show Borrowed Books")
    print("     6. Exit")

    user_choice = int(input())
    if user_choice == 1:
        Harry.displaybooks()

    elif user_choice == 2:
        user = input("Enter your name: ")
        book = input("Enter the name of the book you want to lend: ")
        Harry.lendbook(user, book)

    elif user_choice == 3:
        book = input("Enter the name of the book you want to add: ")
        if book in Harry.booklist:
            print("This book is already available in the library")
        else: 
            Harry.addbook(book)

    elif user_choice == 4:
        user = input("Enter your name: ")
        Harry.returnbook(user)

    elif user_choice == 5:
        Harry.show_lendedbooks()    

    elif user_choice == 6:
        print("Thanks for using the library. Have a great day!")
        break
    else:
        print("Invalid choice! Please try again.")

    go = input("Do you want to continue? (y/n): ").lower()
    if go != 'y' and go != 'yes':
        print("Thanks for using the library. Have a great day!")
        break    