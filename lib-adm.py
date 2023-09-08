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
    # ... (Add book creation logic)
    return redirect(url_for('index'))

@app.route('/add_member', methods=['POST'])
def add_member():
    # ... (Add member creation logic)
    return redirect(url_for('members_list'))

@app.route('/members_list')
def members_list():
    return render_template('members.html', members=members)

@app.route('/delete_book/<int:index>')
def delete_book(index):
    # ... (Add book deletion logic)
    return redirect(url_for('index'))

@app.route('/edit_book/<int:index>', methods=['GET', 'POST'])
def edit_book(index):
    if 0 <= index < len(books):
        book = books[index]
        if request.method == 'POST':
            # Update the book data with the form values
            book.title = request.form['title']
            book.author = request.form['author']
            book.genre = request.form['genre']
            book.isbn = request.form['isbn']
            book.year = request.form['year']
            book.city = request.form['city']
            book.publisher = request.form['publisher']
            return redirect(url_for('index'))
        return render_template('edit_book.html', book=book, index=index)
    return redirect(url_for('index'))

@app.route('/edit_member/<int:index>', methods=['GET', 'POST'])
def edit_member(index):
    if 0 <= index < len(members):
        member = members[index]
        if request.method == 'POST':
            # Update the member's data with the form values
            member.name = request.form['name']
            member.contact = request.form['contact']
            return redirect(url_for('members_list'))
        return render_template('edit_member.html', member=member, index=index)
    return redirect(url_for('members_list'))

@app.route('/delete_member/<int:index>')
def delete_member(index):
    # ... (Add member deletion logic)
    return redirect(url_for('members_list'))

if __name__ == '__main__':
    app.run(debug=True)
