from flask import render_template, request, url_for, redirect, flash, Blueprint
from flask_login import  login_required, current_user
from sqlalchemy import asc, desc, func
from ...models import Contact, Rent, Book
from ...forms import SearchBarForm, AddContact, ContactForm
from app import db

bp = Blueprint('main', __name__)

#Create Contact  

@bp.route('/contacts', methods=['POST','GET'])
@login_required
def cont():
    
    selected_filter =''
    modelBody = ""
    form=SearchBarForm()
    id=current_user.id
    contacts = Contact.query.order_by(asc(Contact.name)).filter_by(user_id=id).all()
    contactsCount = Contact.query.order_by(asc(Contact.name)).filter_by(user_id=id).count()
    searchC =''
    
    
    all_contacts_query = db.session.query(Rent.contact_id).filter_by(user_id=id).distinct()

        # Inicjalizacja pustej listy, która będzie przechowywać wyniki
    contact_rent_counts = []

        # Przejście przez wszystkie id_contact i zliczenie liczby wypożyczonych książek
    for contact_id, in all_contacts_query:
            # Zapytanie, które zwraca liczbę książek wypożyczonych przez konkretny kontakt
            rent_count_query = (
                db.session.query(func.count(Rent.id).label("rent_count"))
                .filter(Rent.contact_id == contact_id)
            )
            
            # Wykonanie zapytania i dodanie wyniku do listy
            rent_count, = rent_count_query.first() or (0,)  # Ustawienie domyślnej wartości na 0, jeśli nie znaleziono wyników
            contact_rent_counts.append([contact_id, rent_count])
    
    if request.method == 'POST':
        db.create_all()
        filter_by = request.form.get("filter_by")        
        searchC = form.searchText.data      
        
        if filter_by == "Email":
            selected_filter = "Email"
            contact2 = Contact.query.filter(Contact.email.contains(searchC)).filter_by(user_id=id).all()
            contactsCount2 = Contact.query.filter(Contact.email.contains(searchC)).filter_by(user_id=id).count()
            return render_template('cont.html', contacts=contact2, contactsCount=contactsCount2, id=id, form=form, contact_rent_counts=contact_rent_counts, selected_filter=selected_filter )

        elif filter_by == "Phone":
            selected_filter = "Phone"
            contact2 = Contact.query.filter(Contact.phone.contains(searchC)).filter_by(user_id=id).all()
            contactsCount2 = Contact.query.filter(Contact.phone.contains(searchC)).filter_by(user_id=id).count()
            return render_template('cont.html', contacts=contact2, contactsCount=contactsCount2, id=id, form=form, contact_rent_counts=contact_rent_counts, selected_filter=selected_filter )
        
        else:
            selected_filter = "Name"
            contact2 = Contact.query.filter(Contact.name.contains(searchC)).filter_by(user_id=id).all()
            contactsCount2 = Contact.query.filter(Contact.name.contains(searchC)).filter_by(user_id=id).count()
            return render_template('cont.html', contacts=contact2, contactsCount=contactsCount2, id=id, form=form, contact_rent_counts=contact_rent_counts, selected_filter=selected_filter )

    return render_template('cont.html', contacts=contacts, contactsCount=contactsCount, id=id, form=form, contact_rent_counts=contact_rent_counts, selected_filter=selected_filter )

#Sortowanie ZA  

@bp.route('/contacts_sort_ZA', methods=['POST','GET'])
@login_required
def contSortZA():
    
    form=SearchBarForm()
    id=current_user.id
    contacts = Contact.query.order_by(desc(Contact.name)).filter_by(user_id=id).all()
    contactsCount = Contact.query.order_by(desc(Contact.name)).filter_by(user_id=id).count()
    searchC =''
    
    if request.method == 'POST':
        db.create_all()
        searchC = form.searchText.data      
        contact2 = Contact.query.filter(Contact.name.contains(searchC)).order_by(desc(Contact.name)).filter_by(user_id=id).all()
        contactsCount2 = Contact.query.filter(Contact.name.contains(searchC)).order_by(desc(Contact.name)).filter_by(user_id=id).count()
        return render_template('cont.html', contacts=contact2, contactsCount=contactsCount2,id=id, form=form )

    return render_template('cont.html', contacts=contacts, contactsCount=contactsCount,id=id, form=form)


#Widok kontaktu    

@bp.route('/contactDetails/<int:id>')
@login_required
def contactDetails(id):
    
    result = db.session.query(Book.id, Contact.id, Book.title, Contact.name, Book.cover_url, Rent.return_date)\
    .join(Rent, Rent.book_id == Book.id)\
    .join(Contact, Contact.id == Rent.contact_id)\
    .all()
    
    
    newId = id
    id=current_user.id
    if request.method == 'GET':     
        contacts2 = Contact.query.filter_by(id=newId)
        return render_template('contactDetails.html', contacts=contacts2, id=id, result=result)

#usuń kontakt

@bp.route('/contactDelate/<int:id>')
@login_required
def contactDelte(id):
    
    contact_to_delete = Contact.query.get_or_404(id)
    
    try:
       db.session.delete(contact_to_delete) 
       db.session.commit()
       flash("Contact Deleted Successfully!!")
    
       return redirect(url_for('cont'))
            
    except:    
       flash("Wooops! can't delete this contact!") 
       return redirect(url_for('cont'))

#Utwórz kontakt

@bp.route("/addContact", methods=['GET','POST'])
@login_required
def addContact():
    form = AddContact()
    id=current_user.id
    
    if request.method == 'GET':
        return render_template('addContact.html', form=form, id=id)
    
    if request.method == 'POST':
        #Validate Form
        if form.validate_on_submit():

            flash("Contact added")
            contact = Contact(name=form.name.data, email=form.email.data, phone=form.phone.data, photo_url='../static/photo.png', user_id=id) 
            db.session.add(contact)
            db.session.commit()
            return redirect(url_for('cont'))
    
    return render_template('addContact.html', form=form, id=id)

#Edytuj kontakt

@bp.route("/editContact/<int:id>", methods=['GET','POST'])
@login_required
def editContact(id):
    
    form = ContactForm()
    contact_to_edit = Contact.query.get_or_404(id)
    id_user=current_user.id
    
    if request.method == 'POST':
        contact_to_edit.name = request.form['name']
        contact_to_edit.email = request.form['email']
        contact_to_edit.phone = request.form['phone']        
        contact_to_edit.note = request.form['note']
        
        try:
            db.session.commit()
            flash("Contact Update Successfully!")
            return redirect(url_for('contactDetails', id=contact_to_edit.id))
        
        except:
            flash("Error!")
            return render_template("editContact.html", form=form, contact_to_edit=contact_to_edit, id=id_user)
    else:
            return render_template("editContact.html", form=form, contact_to_edit=contact_to_edit, id=id_user)