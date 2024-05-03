from flask import Blueprint, render_template, redirect, url_for, request

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if username and password are valid (e.g., compare with database)
    if username == 'valid_username' and password == 'valid_password':
        # Redirect to a different page upon successful login
        return redirect(url_for('main.index'))
    else:
        return 'Invalid username or password'

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # Retrieve signup data from the request and process it
    # e.g., create a new user in the database
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    # Perform logout actions if any
    return redirect(url_for('main.index'))
