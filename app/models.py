from app import db
from datetime import datetime

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column('created_on', db.DateTime, default=datetime.now())
    last_updated = db.Column('last_updated', db.DateTime, onupdate=datetime.now())
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    books = db.relationship('Book', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return '{} {}'.format(self.name, self.surname)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column('created_on', db.DateTime, default=datetime.now())
    last_updated = db.Column('last_updated', db.DateTime, onupdate=datetime.now())
    title = db.Column(db.String(150), index=True)
    description = db.Column(db.String(400))
    year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    copies = db.relationship('Copy', backref='book', lazy='dynamic')
    
    def __repr__(self):
        return 'Book: {} by {}'.format(self.title, self.author)

    def number_of_copies(self):
        return self.copies.count()


class Copy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column('created_on', db.DateTime, default=datetime.now())
    last_updated = db.Column('last_updated', db.DateTime, onupdate=datetime.now())
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    library_serial_number = db.Column(db.String(30))
    date_acquired = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Copy: {}'.format(self.library_serial_number)

class Patron(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column('created_on', db.DateTime, default=datetime.now())
    last_updated = db.Column('last_updated', db.DateTime, onupdate=datetime.now())
    name = db.Column(db.String(40), index=True, nullable=False)
    surname = db.Column(db.String(60), index=True, nullable=False)
    initials = db.Column(db.String(10))
    id_number = db.Column(db.String(20), index=True, unique=True, nullable=False)
    address = db.Column(db.String(50))
    suburb = db.Column(db.String(50))
    city = db.Column(db.String(30))
    postal_code = db.Column(db.String(10))
    email = db.Column(db.String(30), index=True, unique=True)
    phone = db.Column(db.String(15))
    alternative_phone = db.Column(db.String(15))
    next_of_kin = db.Column(db.String(100))
    next_of_kin_relation = db.Column(db.String(30))
    next_of_kin_contact = db.Column(db.String(40))