from flask import render_template, request, url_for, redirect, flash, Blueprint
from flask_login import login_required, current_user
from ...models import Book, Contact, Rent
from ...forms import AddBook
from app import db

bp = Blueprint('main', __name__)

#Utwórz książkę

@bp.route("/addBook", methods=['GET','POST'])
@login_required
def addBook():
    form = AddBook()
    id=current_user.id
    
    if request.method == 'GET':
        return render_template('addBook.html', form=form, id=id, )
    
    if request.method == 'POST':
        #Validate Form
        if form.validate_on_submit():
            rate = request.form.get("rating")
            text_data = form.description.data
            if len(text_data) > 650:
                flash('Text exceeds 850 characters!')
                return render_template('addBook.html', form=form, id=id)
            else:
                message = f"Book {form.title.data} has been added"
                flash(message)
                book = Book(title=form.title.data, author=form.author.data, series=form.series.data, pages=form.pages.data, publisher=form.publisher.data, publishDate=form.publishDate.data, volume=form.volume.data, description=form.description.data, cover_url='../static/cover.png', rate=rate, cover=form.cover.data, user_id=id, isbn=form.isbn.data, note=form.note.data) 
                db.session.add(book)
                db.session.commit()
                return redirect(url_for('index'))
    
    return render_template('addBook.html', form=form, id=id)

#Wyświetl książkę  

@bp.route('/bookDetails/<int:id>')
@login_required
def bookDetails(id):
    
    newId = id
    id=current_user.id
    if request.method == 'GET': 
        
        result = db.session.query(Book.id, Contact.id, Rent.return_date, Contact.name, Contact.photo_url)\
        .join(Rent, Rent.book_id == Book.id)\
        .join(Contact, Contact.id == Rent.contact_id)\
        .all()
        
            
        books2 = Book.query.filter_by(id=newId)
        
        return render_template('bookDetails.html', books=books2, id=id, result=result)


#Edytuj książkę

@bp.route("/editBook/<int:id>", methods=['GET','POST'])
@login_required
def editBook(id):
    
    form = AddBook()
    book_to_edit = Book.query.get_or_404(id)
    id=current_user.id

    if request.method == 'POST':
        book_to_edit.rate = request.form.get("rating")
        book_to_edit.title = request.form['title']
        book_to_edit.author = request.form['author']
        book_to_edit.series = request.form['series']
        book_to_edit.pages = request.form['pages']
        book_to_edit.publisher = request.form['publisher']
        book_to_edit.publishDate = request.form['publishDate']
        book_to_edit.volume = request.form['volume']
        book_to_edit.description = request.form['description']
        book_to_edit.cover = request.form['cover']
        book_to_edit.note = request.form['note']
        book_to_edit.isbn = request.form['isbn']
        try:
            db.session.commit()
            flash("Book Update Successfully!")
            return redirect(url_for('bookDetails', id=book_to_edit.id))
        
        except:
            flash("Error!")
            return render_template("editBook.html", form=form, book_to_edit=book_to_edit, id=id)
    else:
            return render_template("editBook.html", form=form, book_to_edit=book_to_edit, id=id)
        
#usuń książkę  

@bp.route('/bookDelate/<int:id>', methods=['POST','GET'])
@login_required
def bookDelte(id):
    
    book_to_delete = Book.query.get_or_404(id)
    
    try:
       db.session.delete(book_to_delete) 
       db.session.commit()
       flash("Book Deleted Successfully!!")
       
       return redirect(url_for('index'))
            
    except:    
       flash("Wooops! can't delete this book!") 
       return redirect(url_for('index'))