from flask import render_template, request, url_for, redirect, flash, Blueprint 
from datetime import datetime, timedelta
from flask_login import login_required, current_user
from ...models import Book, Contact, Rent
from ...forms import BookRentForm
from app import db

bp = Blueprint('main', __name__)

#Wypożyczenie książki

@bp.route('/rentBook/<int:id>', methods=['POST','GET'])
@login_required
def rentBook(id):
    date = datetime.today()
    return_date = datetime.today()+timedelta(days=30)
    formated_return_date = return_date.strftime("%d/%m/%y")
    
    newId = id
    
    form=BookRentForm()
    book_to_rent = Book.query.get_or_404(id)
    borrower = ''
    id=current_user.id
    
    if request.method == 'GET':           
        books2 = Book.query.filter_by(id=newId)
        contact2 = Contact.query.filter_by(user_id=current_user.id).all() 
        return render_template('rentBook.html', books=books2, contacts=contact2, id=id, date=date, return_date=return_date, form=form, book_to_rent=book_to_rent, borrower=borrower)
   
    if request.method == 'POST':
        borrower = request.form.get('borrower')
        book_to_rent.note = request.form['note']
        name = borrower 
        borrowerName = Contact.query.filter_by(name=name).first()     
        try:
                message = f"Book {book_to_rent.title} has been borrowed to {borrowerName} until {formated_return_date}"
                flash(message)
                book_to_borrow = Book.query.get_or_404(book_to_rent.id)
                book_to_borrow.status = True
                contact_borrower = Contact.query.get_or_404(borrowerName.id)
                contact_borrower.status = True
                
                rent = Rent(borrow_date=date, return_date=return_date, book_id=book_to_rent.id, contact_id=borrowerName.id, user_id=current_user.id) 
                db.session.add(rent)
                db.session.commit()
                return redirect(url_for('index'))
        except:
            return redirect(url_for('index'))
    else:
            return redirect(url_for('index'))

#Zwracanie książki

@bp.route('/returnBook/<int:id>', methods=['POST','GET'])
@login_required
def returnBook(id):
    
    newId = id
    
    form=BookRentForm()
    book_to_return = Book.query.get_or_404(id)
    borrower = ''
    id=current_user.id
    rents = Rent.query.filter_by(book_id=newId).all()
    
    result_count = db.session.query(Book.id, Contact.id, Book.title, Contact.name)\
        .join(Rent, Rent.book_id == Book.id)\
        .join(Contact, Contact.id == Rent.contact_id)\
        .filter_by(user_id=id)\
        .count()
     
    for rent in rents: 
        rent_id = rent.id
        contact_id = rent.contact_id
        contact2 = Contact.query.filter_by(id=contact_id) 
        
    
    if request.method == 'GET':
        if Rent.query.filter_by(book_id=newId).count() > 0:        
            books2 = Book.query.filter_by(id=newId)
            return render_template('returnBook.html', books=books2, contacts=contact2, id=id, form=form, book_to_return=book_to_return, borrower=borrower)
   
    if request.method == 'POST':
              book_to_return.note = request.form['note']
              for cont in contact2: 
                c=cont.name
                contact_return_id=cont.id 
                try:
                    rent_to_delete = Rent.query.get_or_404(rent_id)
                    db.session.delete(rent_to_delete)
                    db.session.commit()
                    message = f"Book {book_to_return.title} has been returned from {c}"
                    flash(message)
                    
                    book_return = Book.query.get_or_404(book_to_return.id)
                    book_return.status = False
                    db.session.commit()
                    
                    if result_count == 0:
                        contact_borrower = Contact.query.get_or_404(contact_return_id)
                        contact_borrower.status = False
                        db.session.commit()
                        
                
                    return redirect(url_for('index'))
                except:
                    return redirect(url_for('index'))
    else:
            return redirect(url_for('index'))