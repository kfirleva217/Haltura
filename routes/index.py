from flask import render_template, request, redirect, url_for
from app import app, db
from routes.models import Handyman
from .forms import RegistrationForm


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()  # Create an instance of the form

    if form.validate_on_submit():
        new_user = Handyman(email=form.email.data, username=form.username.data, password=form.password.data,
                            user_type=form.user_type.data, state=form.state.data, full_name=form.full_name.data,
                            about_yourself=form.about_yourself.data, occupation=form.occupation.data,
                            experience=form.experience.data)

        db.session.add(new_user)
        db.session.commit()

        return "User registered successfully!"

    return render_template('signup.html', form=form)
