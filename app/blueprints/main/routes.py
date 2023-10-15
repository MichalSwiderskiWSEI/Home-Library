from flask import render_template, request, Blueprint
from flask_login import login_required, current_user
from sqlalchemy import asc, desc, func

from ...models import Book, Contact, Rent
from ...forms import SearchBarForm
from app import db

bp = Blueprint('main', __name__)


#home page

@bp.route('/')
def home():
    return render_template('home.html')

#index

@bp.route('/home', methods=['POST','GET'])
@login_required
def index():
    
    form=SearchBarForm()
    selected_filter ='Title'
    
    result = db.session.query(Book.id, Contact.id, Book.title, Contact.name)\
        .join(Rent, Rent.book_id == Book.id)\
        .join(Contact, Contact.id == Rent.contact_id)\
        .all()
           
    id=current_user.id
    
    books = Book.query.filter_by(user_id=id).order_by(asc(Book.title)).all()   
    booksCount = Book.query.order_by(asc(Book.title)).filter_by(user_id=id).count()
    searchB = ''
    
    
    if request.method == 'POST':
        filter_by = request.form.get("filter_by")     
        searchB = form.searchText.data 
 
       
        if filter_by == "Author":
                sorting_by_za = False
                books2 = Book.query.filter(Book.author.contains(searchB)).filter_by(user_id=id).order_by(asc(Book.author), desc(Book.title)).all()    
                booksCount2 = Book.query.filter(Book.author.contains(searchB)).filter_by(user_id=id).count()

                return render_template('index.html', books=books2, booksCount=booksCount2, id=id, form=form, result=result, selected_filter=selected_filter) 
            
        elif filter_by == "Series":
                selected_filter = "Series"
                books2 = Book.query.filter(Book.series.contains(searchB)).filter_by(user_id=id).order_by(asc(Book.series)).all()
                booksCount2 = Book.query.filter(Book.series.contains(searchB)).filter_by(user_id=id).count()

                return render_template('index.html', books=books2, booksCount=booksCount2, id=id, form=form, result=result, selected_filter=selected_filter)
        
        else:
                selected_filter = "Title"
                books2 = Book.query.filter(Book.title.contains(searchB)).filter_by(user_id=id).order_by(asc(Book.title)).all()
                booksCount2 = Book.query.filter(Book.title.contains(searchB)).filter_by(user_id=id).count()

                return render_template('index.html', books=books2, booksCount=booksCount2, id=id, form=form, result=result, selected_filter=selected_filter) 
        
  
    #print(booksCount) 
    return render_template('index.html', books=books, booksCount=booksCount, id=id, form=form, result=result, selected_filter=selected_filter)
