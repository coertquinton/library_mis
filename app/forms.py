from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, HiddenField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

class CreateAuthorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    submit = SubmitField('Create Author')

class CreateBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    year = StringField('Year')
    author_id = SelectField(u'Author', coerce=int)
    submit = SubmitField('Create Book')

class CreateCopy(FlaskForm):
    book_id = HiddenField("Book ID")
    book = StringField('Book')
    library_serial_number = StringField('Library Serial Number', validators=[DataRequired()])
    date_acquired = DateField('DatePicker', format='%Y-%m-%d')
    submit = SubmitField('Create Copy')
