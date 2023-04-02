from flask import Blueprint, render_template

views = Blueprint('views', '__name__')

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/csgo')
def csgo():
    return render_template('csgo.html')

@views.route('/valorant')
def valorant():
    return render_template('valorant.html')