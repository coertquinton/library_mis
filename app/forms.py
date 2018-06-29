from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, HiddenField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, NumberRange

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

class CreatePatronForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    initials = StringField('Initials', validators=[DataRequired()])
    id_number = StringField('ID Number', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    suburb = StringField('Suburb')
    city = StringField('City', validators=[DataRequired()])
    postal_code = StringField('Postal Code')
    email = StringField('Eail', validators=[Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    alternative_phone = StringField('Alternative Phone')
    next_of_kin = StringField('Next of Kin', validators=[DataRequired()])
    next_of_kin_relation = StringField('Kin Relationship', validators=[DataRequired()])
    next_of_kin_contact = StringField('Kin Contact', validators=[DataRequired()])
    submit = SubmitField('Create Patron')
