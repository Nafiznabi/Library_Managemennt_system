# Implementing a library system

# Creating a class Book representing books in a libarary in which strings:Tittle, author, ISBN are pased 
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    # diplay all the information regrading the title ,author and isbn
    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class EBook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Format: {self.file_format}"


class Library:
    def __init__(self):
        self.books = []    #creating a list named books that stores all the books

    def add_book(self, book):    #adding a book in the books list
        if not isinstance(book, Book):     #check if the book belongs to the following instance books or not by using isistance
            return "value error" #if not raise a value error
        self.books.append(book)      #valid name of the book the book is added to the list

    def display_books(self): #displaying all the books present in the list named books or in the library
        if not self.books:
            return "No books in the library."
        book_info = [book.display_info() for book in self.books]   #print all the information regarding the book using list comprehension method
        return "\n".join(book_info)           #display all the informataion regarding to the 

    def search_by_title(self, title):   #passing title in the function to search based uponn the title
        found_books = [book for book in self.books if book.title.lower() == title.lower()]  #searching done and get the details of the book with the required title
        if not found_books:
            return "Book not found."
        return "\n".join([book.display_info() for book in found_books])


# Example of usage:

book1 = Book("The Great Gatsby","Nafiz Nabi", "978-3-16-148410-0")
book2 = EBook("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0", "PDF")
book3= Book("Introduction to algorihtm","THomas H.Cormen", "978-3-16-148411-0")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("All Books in Library:")
print(library.display_books())

search_title = "the great gatsby"
print(f"\nSearch Results for '{search_title}':")
print(library.search_by_title(search_title))

# except ValueError as e:
#     print(f"Error: {e}")
