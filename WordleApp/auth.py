from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import current_user
from flask_login import login_user,login_required,logout_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/document_help')
def document_help():
    return render_template('document_help.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    
    # if the above check passes, then we know the user has correct credentials
    login_user(user, remember=remember)

    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup',methods=['POST'])
def signup_post():
    #code to validate user to db
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # check if the user with same email already exist in the system.
    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    
    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256')) # pbkdf2: was recommeded by chatgpt and this worked (here's link to it's documentation: https://werkzeug.palletsprojects.com/en/3.0.x/)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required # because it does make sense to log out use that is not logged in.
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# Getting the Score for the User:

from WordleApp.game_data import add_score, get_scores

@auth.route('/game_play',methods=['POST'])
@login_required
def game_play():
    try:
        # Retrieve form data
        score = request.form.get('score')
        attempts = request.form.get('attempts')
        time_needed= request.form.get('time_taken')

        # Assuming add_game_data is a function in game_data.py that adds the game stats to the database
        # print('I will be adding scores')
        add_score(score, attempts,time_needed)
        # print('scores already addded')


        # Redirect to another page (e.g., the leaderboard) or back to the form
        print('redirected to authleadershboard')
        return redirect(url_for('auth.leaderboard'))  # 
    
    except Exception as e:
        # Log the exception; for now, we print it
        print(f"Error processing the game data: {e}")
        flash(f"An error occurred: {e}", 'error')  # Display error message to the user
        return redirect(url_for('auth.game_play'))  # Optionally redirect back to the form



@auth.route('/leaderboard')
@login_required
def leaderboard():
    # user = User.query.filter_by(email=email).first()
    scores = get_scores(user_id=current_user.id)
    # print(scores,current_user.id)
    scores = [
        {'date': score.date.strftime('%Y-%m-%d'), 'score': score.score, 'attempts': score.attempts,'time_taken':score.time_taken}
        for score in scores]
    
    return render_template('leaderboard.html',scores=scores)

