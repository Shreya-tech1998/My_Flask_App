from flask import Blueprint, render_template, url_for, request,redirect,jsonify
from .models import TESTING123, USERS
import cx_Oracle

auth = Blueprint('auth', __name__)


@auth.route('/signup')
def signup():
    print("I'm in signup")
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    
    if request.is_json:
     USER_NAME = request.json.get('name')
     EMAIL = request.json.get('email')
     passphrase = request.json.get('passphrase')

    else:
        return jsonify({'success': False, 'message': 'Invalid request format. Content-Type must be application/json.'})

 
    # Check if the user already exists
    existing_user = USERS.query.filter_by(EMAIL=EMAIL.lower()).first()
    if existing_user:
            return jsonify({'success': False, 'message': 'User already exists'})
    
     # Call the add_user stored procedure
    #connection = cx_Oracle.connect(user='BULLFLIX_PY', password='usf1956!', dsn='reade.forest.usf.edu:1521/cdb9')
    
    #connection = cx_Oracle.connect('BULLFLIX_PY/usf1956!@reade.forest.usf.edu:1521/cdb9')
    #cursor = connection.cursor()
    conStr = 'BULLFLIX_PY/usf1956!@reade.forest.usf.edu:1521/cdb9'
    connect = cx_Oracle.connect(conStr)
    cur = connect.cursor()

    # Prepare the call to the stored procedure
    return_int = cur.var(cx_Oracle.NUMBER)
    cur.callproc('BULLFLIX.ADD_USER', [USER_NAME, EMAIL, passphrase, return_int])
    connect.commit()
    
    # Check the return_int value to determine success
    if return_int.getvalue() == 1:
            print("success")
    else:
         print("updation failed")            
        
    cur.close()
    connect.close()     
    return redirect(url_for('auth.login'))


@auth.route('/login')
def login():
    print("In Initial Login")
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    #email = request.form.get('email')
    #password = request.form.get('password')
    #remember = True if request.form.get('remember') else False
    if request.is_json:     
     EMAIL = request.json.get('email')
     passphrase = request.json.get('passphrase')

    else:
        return jsonify({'success': False, 'message': 'Invalid request format. Content-Type must be application/json.'})
    # autenticate the user if they exist then take all the movies recommended for them and display it
    # if user does not exist then redirect them to the signup page
    conStr = 'BULLFLIX_PY/usf1956!@reade.forest.usf.edu:1521/cdb9'
    oracle_connection = cx_Oracle.connect(conStr)
    try:
        cursor = oracle_connection.cursor()

        # Call the stored procedure
        user_hex_guid = cursor.var(cx_Oracle.STRING)
        print("Before Call proc")
        cursor.callproc('BULLFLIX.AUTHENTICATE_USER', [EMAIL, passphrase,user_hex_guid])
        print(user_hex_guid)
        print("After Callproc")

        # Check the result of the authentication
        if user_hex_guid.getvalue():
            # Authentication successful, redirect to the profile page
            # also display the recommended movies to this profile
            return redirect(url_for('main.profile'))
        else:
            # Authentication failed, redirect to the signup page
            print("There is no user like this")
            return redirect(url_for('auth.signup'))

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("Oracle Database Error:", error)
        

    finally:
        cursor.close()
        oracle_connection.close()
    

    return redirect(url_for('auth.signup'))


@auth.route('/logout')
def logout():
    return "Use this to log out."