from flask import render_template, flash, redirect, url_for

from app.models import Author, Book, Copy
from app.forms import CreateAuthorForm, CreateBookForm, CreateCopy
from app.display_items import AuthorTable, BookTable, CopiesTable

from app import app, db

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/create_author', methods=['GET', 'POST'])
def create_author(id=None):
    form = CreateAuthorForm()
    if form.validate_on_submit():        
        author = Author(name=form.name.data, surname=form.surname.data)
        db.session.add(author)
        db.session.commit()
        flash('Created author {} {}...'.format(form.name.data, form.surname.data))
        
        return redirect('/authors')

    return render_template('create_author.html', form=form)


@app.route('/authors')
def authors():
    authors = Author.query.order_by('id')

    table = AuthorTable(authors)
    return render_template('authors.html', title='Authors', table=table)


@app.route('/edit_author/<id>', methods=['GET', 'POST'])
def edit_author(id=None):
    form = CreateAuthorForm()
    if form.validate_on_submit():
        if id:
            authors = Author.query.filter_by(id=id)
            if authors:
                author = authors[0]
                author.name = form.name.data
                author.surname = form.surname.data
                db.session.commit()
                flash('Author updated')
                flash('Author updated')
            flash('No valid author found')

        flash('Author details updated')
        return redirect('/authors')

    if id:
        authors = Author.query.filter_by(id=id)
        if authors:
            form = CreateAuthorForm(obj=authors[0])
    return render_template('edit_author.html', form=form)


@app.route('/create_book', methods=['GET', 'POST'])
def create_book():
    form = CreateBookForm()
    form.author_id.choices = [(a.id, a) for a in Author.query.all()]
    if form.validate_on_submit():
        book = Book(title=form.title.data, description=form.description.data,
                    author_id=form.author_id.data, year=form.year.data)
        db.session.add(book)
        db.session.commit()
        flash('Created book {} {}...'.format(form.title.data, form.description.data))

        return redirect('/books')

    return render_template('create_book.html', form=form)


@app.route('/books')
def books():
    books = Book.query.order_by('id')

    table = BookTable(books)
    return render_template('books.html', title='Books', table=table)


@app.route('/edit_book/<id>', methods=['GET', 'POST'])
def edit_book(id=None):
    form = CreateBookForm()
    form.author_id.choices = [(a.id, a) for a in Author.query.all()]
    if form.validate_on_submit():
        if id:
            books = Book.query.filter_by(id=id)
            if books:
                book = books[0]
                if form.title.data:
                    book.title = form.title.data
                if form.description.data:
                    book.description = form.description.data
                if form.year.data:
                    book.year = form.year.data
                book.author_id = form.author_id.data
                db.session.commit()
                flash('Book updated')
                flash('Book updated')
            flash('No valid book found')

        flash('Book details updated')
        return redirect('/books')

    if id:
        books = Book.query.filter_by(id=id)
        if books:
            form = CreateBookForm(obj=books[0])
            form.author_id.choices = [(a.id, a) for a in Author.query.all()]

            #get us copies
            copies = Copy.query.filter_by(book_id=books[0].id)
            copies_table = CopiesTable(copies)

    return render_template('edit_book.html', form=form, book_id=books[0].id, copies_table=copies_table)


@app.route('/create_copy/<id>', methods=['GET', 'POST'])
def create_copy(id=None):
    form = CreateCopy()

    if form.validate_on_submit():
        copy = Copy(book_id=int(form.book_id.data), library_serial_number=form.library_serial_number.data,
                    date_acquired=form.date_acquired.data.strftime('%Y-%m-%d'))
        db.session.add(copy)
        db.session.commit()

        return redirect('/edit_book/{}'.format(form.book_id.data))

    books = Book.query.filter_by(id=int(id))
    print(books)
    if books:
        book = books[0]
        form.book.data = book
        form.book_id.data = book.id
        return render_template('create_copy.html', form=form)

    return redirect('/books')


    
    
    


