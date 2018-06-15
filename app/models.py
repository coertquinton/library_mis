from app import db

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
    
    def __repr__(self):
        return '<Book {}>'.format(self.title)
