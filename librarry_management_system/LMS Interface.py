from flask import Flask, request, jsonify
from assignment import Library,EBook,Book

app = Flask(__name__)

library = Library()

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    try:
        if data.get('file_format'):
            book = EBook(data['title'], data['author'], data['isbn'], data['file_format'])
        else:
            book = Book(data['title'], data['author'], data['isbn'])
        library.add_book(book)
        print(f"Book added: {book.display_info()}")
        return jsonify({"message": "Book added successfully."}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

@app.route('/list_books', methods=['GET'])
def list_books():
    books_info = [book.display_info() for book in library.books]
    return jsonify({"books": books_info})

if __name__ == '__main__':
    app.run(debug=True)
