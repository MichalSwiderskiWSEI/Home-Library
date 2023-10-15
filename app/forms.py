from flask_wtf import FlaskForm

class AddBook(FlaskForm):
    title = StringField("What is the book title?", validators=[DataRequired()])
    author = StringField("What is the book author?", validators=[DataRequired()])
    series = StringField("What is the book series?")
    pages = StringField("What is the book pages?")
    publisher = StringField("What is the book publisher?")
    publishDate = StringField("What is the book publishDate?")
    volume = StringField("What is the book volume?")
    description = StringField("What is the book description?", widget=TextArea())
    rate = StringField("What is the book rate?")
    cover_url = StringField("What is the book cover_url?")
    cover = StringField("What is the book cover?")
    isbn = StringField("What is the book cover?")
    submit = SubmitField("Add Book")
    note = SubmitField("test", widget=TextArea())

class AddContact(FlaskForm):
    name = StringField("What is the contact name?", validators=[DataRequired()])
    email = StringField("What is the contact email?", validators=[DataRequired()])
    phone = StringField("What is the contact phone?", validators=[DataRequired()])
    photo_url = StringField("What is the contact photo_url?")
    note = SubmitField("test", widget=TextArea())
    submit = SubmitField("Add Contact")
       
class UserForm(FlaskForm):
    username = StringField("What is your username?", validators=[DataRequired()])
    email = StringField("What is your email?", validators=[DataRequired()])
    password_hash = PasswordField("Password", validators=[DataRequired(), EqualTo('password_hash2', message='Password Must Match!')] ) 
    password_hash2 = PasswordField("Confirm Password", validators=[DataRequired()])
    photo_url = StringField("What is the contact photo_url?")
    note = SubmitField("test", widget=TextArea())
    submit = SubmitField("sign Up")
    
class BookRentForm(FlaskForm):
    name = StringField()
    note = StringField()
    submit = SubmitField("test", widget=TextArea())

class UserEditForm(FlaskForm):
    email = StringField()
    password_hash = PasswordField() 
    password_hash2 = PasswordField()
    note = SubmitField("test", widget=TextArea())
    submit = SubmitField()    

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()] )
    remember_me = BooleanField("remember Me")
    submit = SubmitField("sign In")
    
class ContactForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    email = StringField("What is your email?", validators=[DataRequired()])
    phone = StringField("What is your email?", validators=[DataRequired()])
    note = SubmitField("test", widget=TextArea())
    submit = SubmitField("Update")    
    
class SearchBarForm(FlaskForm):
    searchText = StringField("What do you search?", validators=[DataRequired()])
    radioPick = StringField("What do you prefer?", validators=[DataRequired()])       
    submit = SubmitField("")  

class UploadForm(FlaskForm):
    images = FileField('', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    note = SubmitField("test", widget=TextArea())
    submit = SubmitField("Update")     