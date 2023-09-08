from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data sementara untuk buku dan anggota perpustakaan
books = []
members = []

class Book:
    def __init__(self, title, author, genre, isbn, copies, year, city, publisher):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.copies = copies
        self.year = year  # Menambahkan atribut tahun
        self.city = city  # Menambahkan atribut kota
        self.publisher = publisher  # Menambahkan atribut penerbit

class Member:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

@app.route('/')
def index():
    return render_template('index.html', books=books, members=members)

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    isbn = request.form['isbn']
    copies = int(request.form['copies'])
    year = request.form['year']  # Mengambil tahun dari formulir
    city = request.form['city']  # Mengambil kota dari formulir
    publisher = request.form['publisher']  # Mengambil penerbit dari formulir

    new_book = Book(title, author, genre, isbn, copies, year, city, publisher)
    books.append(new_book)

    return redirect(url_for('index'))

@app.route('/add_member', methods=['POST'])
def add_member():
    name = request.form['name']
    contact = request.form['contact']

    new_member = Member(name, contact)
    members.append(new_member)

    return redirect(url_for('members_list'))

@app.route('/members_list')
def members_list():
    return render_template('members.html', members=members)

@app.route('/delete_book/<int:index>')
def delete_book(index):
    if 0 <= index < len(books):
        del books[index]
    return redirect(url_for('index'))

@app.route('/edit_book/<int:index>', methods=['GET', 'POST'])
def edit_book(index):
    if 0 <= index < len(books):
        book = books[index]
        if request.method == 'POST':
            # Update the book data with the form values
            book.title = request.form['title']
            book.author = request.form['author']
            # ... (update other attributes)

            return redirect(url_for('index'))
        return render_template('edit_book.html', book=book)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
