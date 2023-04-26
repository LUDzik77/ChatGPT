from flask import Flask, request, jsonify
#from books import list_of_books  as b


app = Flask(__name__)

#books_list = books.b
list_of_books = [
    {
        "id": 1,
        "author":"R.Service",
        "language":"polish",
        "title":"Szpiedzy i komisarze",
    },
    {
        "id": 2,
        "author":"Starkov",
        "language":"french",
        "title":"Russe de guerre",
    },
    {
        "id": 3,
        "author":"Dukaj",
        "language":"polish",
        "title":"Po piśmie",
    },
    {
        "id": 4,
        "author":"M.Żelkowski",
        "language":"polish",
        "title":"Wojna cieni",
    },
    {
        "id": 5,
        "author":"Lem",
        "language":"polish",
        "title":"Solaris",
    },
    {
        "id": 6,
        "author": "ph:DOSNE",
        "language":"english",
        "title":"The Illustrated biography of Salvador Dali",
    }
    ]

@app.route('/books', methods=['GET','POST'])
def books():
    if request.method =='GET':
        if len(books_list) > 0:
            return(jsonify(books_list))
        else: 'Nothing Found', 404
    if request.method == 'POST':
        new_author = request.form['author']
        new_language = request.form['language']
        new_title = request.form['title']
        iD = books_list[-1]['id']+1     #to test
    
    new_obj = {
        "id": iD,
        "author": new_author,
        "language": new_language,
        "title": new_title    
        }
    books_list.append(new_obj)
    # HTTP 201  = Created success status response code 
    return(jsonify(books_list), 201)


@app.route('/book/<int:id>', methods=['GET','PUT','DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return(jsonify(book))
            pass
    if request.method == 'PUT':
        for book in books_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['language'] = request.form['language']
                book['title'] = request.form['title']
                updated_book = {
                    'id': id,
                    'author': book['author'],
                    'language': book['language'],
                    'title': book['title']
                    }
                return jsonify(updated_book)

if __name__ == "__main__":
    app.run()