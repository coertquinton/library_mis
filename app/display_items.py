from flask_table import Table, Col, LinkCol

class AuthorTable(Table):

    name = Col('Name')
    surname = Col('Surname')
    id = LinkCol('Edit', 'edit_author', url_kwargs=dict(id='id',face='name'))


class BookTable(Table):

    title = Col('Title')
    description = Col('Description')
    year = Col('Year')
    author = Col('Author')
    number_of_copies = Col('Copies')
    id = LinkCol('Edit', 'edit_book', url_kwargs=dict(id='id'))

class CopiesTable(Table):

    date_acquired = Col('Date Acquired')
    library_serial_number = Col('Serial Number')
