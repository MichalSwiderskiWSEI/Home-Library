from flask import render_template, request, url_for, redirect, flash, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from ...models import User
from ...forms import UserForm, UserEditForm, UploadForm
from app import db

bp = Blueprint('main', __name__)

#utwórz użytkownika

@bp.route('/signUp', methods=['GET','POST'])
def signUp():
    form = UserForm()
    
    if request.method == 'GET':
        return render_template('signUp.html', form=form)
    
    if request.method == 'POST':
        username = form.username.data
        print(form.username.data)
        #Walidacja Formy
        searchUser = User.query.filter(User.username==form.username.data).all()
        
        if searchUser:          
            message = f"User {username} already exist. Please login."
            flash(message)
            return redirect(url_for('login'))
        else:
            if form.validate_on_submit():
                message = f"User {username} added. Please login."
                flash(message)
                user = User(username=form.username.data, email=form.email.data, password=form.password_hash.data) 
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))
    
    return render_template('signUp.html', form=form)

#Utwórz widok użytkownika    

@bp.route('/userOption/<int:id>')
@login_required
def userOption(id):
    
    user_id = id
        
    if request.method == 'GET':        
        user2 = User.query.filter_by(id=user_id)
        return render_template('userOptions.html', users=user2, id=id )

#Edytuj użytkownika   
    
@bp.route("/editUser/<int:id>", methods=['POST','GET'])
def editUser(id):
    
    form = UserEditForm()
    user_to_edit = User.query.get_or_404(id)

    if request.method =='GET':
        return render_template('editUser.html', form=form, user_to_edit=user_to_edit, id=id)

    print(user_to_edit.id)
    if request.method =='POST':
        
        user_to_edit.email = request.form['email']                   
        user_to_edit.note = request.form['note']
        print(user_to_edit.note)        
        if request.form['password_hash']: 
            user_to_edit.password_hash = generate_password_hash(request.form['password_hash'], 'sha256')  
        
        try:
            #Walidacja Formy
            if form.validate_on_submit():               
                username = current_user.username
                message = f"user { username } update completed!"              
                flash(message)              
                db.session.commit()               
                return redirect(url_for('userOption', id=current_user.id))     
        except:
            message = f"Update faild. Please try again!"              
            flash(message) 
            return render_template('editUser.html', form=form, user_to_edit=user_to_edit, id=id)

    else:
            message = f"Update faild. Please try again!"              
            flash(message) 
            return render_template('editUser.html', form=form, user_to_edit=user_to_edit, id=id)

#Wstawianie zdjęcia użytkownika  

@bp.route("/upload/<int:id>", methods=['GET', 'POST'])
def upload(id):
    form = UploadForm()
    
    id=current_user.id
    
    user_to_edit = User.query.get_or_404(id)
    
    if form.validate_on_submit():
        for image in request.files.getlist('images'):
            filename = secure_filename(image.filename)
            image.save(os.path.join(....config['UPLOAD_PATH'], filename))
            photo_url =f'../static/{filename}'
            user_to_edit.photo_url = photo_url
            db.session.commit() 
            return redirect(url_for('userOption', id=user_to_edit.id))
    
    return render_template('upload.html', form=form, id=id, user_to_edit=user_to_edit)
