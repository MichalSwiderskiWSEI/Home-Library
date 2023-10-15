from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(60), nullable=False)
    series = db.Column(db.String(100))
    pages = db.Column(db.String(100))
    publisher = db.Column(db.String(100))
    publishDate = db.Column(db.String(100))
    volume = db.Column(db.String(10))
    description = db.Column(db.String(1500))
    rate = db.Column(db.String(5))
    status = db.Column(db.Boolean)
    cover_url = db.Column(db.String(100))
    cover = db.Column(db.String(20))
    isbn = db.Column(db.String(20))
    note = db.Column(db.String(450))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    
    loans = db.relationship('Rent', backref='book', lazy='dynamic')
    

    # Create A String
    def __repr__(self):
        return self.title
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    photo_url = db.Column(db.String(100))
    loans = db.relationship('Rent', backref='user', lazy=True)
    books = db.relationship('Book', backref='user', lazy=True)
    note = db.Column(db.String(450))
    contacts = db.relationship('Contact', backref='user', lazy=True)
    
    @property 
    def password(self):
        raise AttributeError('Wrong Password')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)        
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # Create A String
    def __repr__(self):
        return self.username
    
    
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(9), nullable=False)
    photo_url = db.Column(db.String(100))
    status = db.Column(db.Boolean)
    note = db.Column(db.String(450))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    
    loans = db.relationship('Rent', backref='contact', lazy=True)
    
    # Create A String
    def __repr__(self):
        return self.name
    
class Rent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrow_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime)  
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)  
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'), nullable=False) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 

    
    # Create A String
    def __repr__(self):
        return '%r' % self.id