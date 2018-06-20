from app import db
from datetime import datetime

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    books = db.relationship('Book', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return '{} {}'.format(self.name, self.surname)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), index=True)
    description = db.Column(db.String(400))
    year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    copies = db.relationship('Copy', backref='book', lazy='dynamic')
    
    def __repr__(self):
        return '<Book {} by {}>'.format(self.title, self.author)

    def number_of_copies(self):
        return self.copies.count()


class Copy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    library_serial_number = db.Column(db.String(30))
    date_acquired = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Copy> {}'.format(self.library_serial_number)