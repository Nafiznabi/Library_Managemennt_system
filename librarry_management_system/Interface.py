from flask import Flask, request, jsonify
from Code import Library
from Code import EBook
from Code import Book

app = Flask(__name__)

library = Library()

@app.route('/add_book', methods=['POST'])     #defining the route for the flaask application 
def add_book():
    data = request.get_json() #retrives JSON data from HTTP request body and stores it in data variable
    try:
        if data.get('file_format'):
            book = EBook(data['title'], data['author'], data['isbn'], data['file_format'])
        else:
            book = Book(data['title'], data['author'], data['isbn'])
        library.add_book(book)      #call the add_book method of the library
        print(f"Book added: {book.display_info()}")
        return jsonify({"message": "Book added successfully."}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

@app.route('/list_books', methods=['GET'])
def list_books():
    app.logger.info("Listing books...")
    books_info = [book.display_info() for book in library.books]
    app.logger.info(f"Books in the library: {books_info}")
    return jsonify({"books": books_info})


@app.route('/')
def index():
    return "welcome to the page"
if __name__ == '__main__':
    app.run(debug=True)
