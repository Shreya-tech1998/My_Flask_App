from flask import Blueprint, render_template
from .models import TESTING123, USERS


main = Blueprint('main', __name__)


@main.route('/')
def index():
    #records = USERS.query.all()
    #for record in records:
    #print(record.USER_NAME)   
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')

