'''
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login#step-1-installing-packages
'''

from flask import Blueprint, render_template
from flask_login import login_required,current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required # login is requred to see the profile.
def profile():
    return render_template('profile.html',name=current_user.name)

@main.route('/game_play')
@login_required # login is requred to see the game play
def game_play():
    return render_template('game_play.html',name=current_user.name)
