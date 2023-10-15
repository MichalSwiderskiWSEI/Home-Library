from flask import Blueprint
from flask import render_template, request, url_for, redirect, flash
from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, logout_user
from ...models import User
from ...forms import LoginForm

bp = Blueprint('auth', __name__)

#Strona logowania 
 
@bp.route('/login', methods=['GET', 'POST'])
def login():
     form = LoginForm()
     
     if request.method == 'GET':
        return render_template('login.html', form=form)
    
     if request.method == 'POST':
        user = User.query.filter_by(username=form.username.data).first()
        if user:
             if check_password_hash(user.password_hash, form.password.data):
                login_user(user, remember=form.remember_me.data)
                message = f"Login Succesfull!! Welcome {form.username.data} to your Home Library."
                flash(message)
                return redirect(url_for('index'))
             else:
                 flash("Wrong Password - Try Again!")
                 return redirect(url_for('login'))
        else:
             flash("That User Doesn't Exist! Try Again...")
             return render_template('login.html', form=form)

#Wyloguj się

@bp.route('/logout',methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You are log out!')
    
    return redirect('login')