from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, current_user, logout_user


from . import auth
from .forms import LoginForm, RegistrationUser
from ..models import User
from .. import db

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.user', username=current_user.username))
        
    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationUser()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                password=form.password.data,
                username=form.username.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)
