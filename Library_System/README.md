# 📚 Library Management Project in Python

A simple command-line program for managing a library, allowing you to display, lend, add, and return books.

## Features

- **Display Books**: Shows the list of available books in the library.
- **Lend a Book**: Borrow a book by entering your name for 30 days.
- **Add a Book**: Add a new book to the library.
- **Return a Book**: Return a previously borrowed book.
- **Show Borrowed Books**: View the list of borrowed books and borrowers' names.
- **Exit**: End the program with a goodbye message.

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Copy the code into a file named `library.py`.
3. Open the command line and run the program:
   ```bash
   python library.py
   ```
4. Follow the instructions on the screen and enter the number of your chosen option.

## Example Run

```
______Welcome to the CodeWithHarry Library______
Enter your choice to continue: 
     1. Display Books
     2. Lend a Book
     3. Add a Book
     4. Return a Book
     5. Show Borrowed Books
     6. Exit
```

- Choose the desired option and enter the required data (your name, book name).
- You can continue or exit after each operation as you wish.

## Technical Notes

- The program converts book names to lowercase internally to avoid duplicates due to case differences.
- Borrowed books status is saved only during the running session (no persistent storage).
- The code is easy to extend and modify as needed.

---
This is a simple educational program to help you learn basic object-oriented programming in Python and manage data using lists and dictionaries.
