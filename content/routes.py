# Local application imports
from content import mysql, mail, app
from .appoint_tag_gen import randomDigits
from .contact import sendEmail, replyMessage, reset_password_link
from .form import ChangepswdForm
from .token import TokenGEN
from .views import ProfileEndpoint


# Third party imports
from flask import render_template, request, redirect, url_for, flash, session, Markup
from passlib.hash import sha256_crypt  # Encrypts password
from functools import wraps


# Standard library import
import os
from datetime import datetime as dt


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, *kwargs)
        else:
            flash('Unauthorized Access, Please make sure you are logged in', 'danger')
            return redirect(url_for('login'))
    return wrap


def not_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            flash('Unauthorized, You are already logged in', 'danger')
            return redirect(url_for('user_dashboard'))
        else:
            return f(*args, *kwargs)
    return wrap



# Route for index
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html'), 200


# Route for about
@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html'), 200

    
# Route for contact
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        inputName = request.form['contactName']
        inputEmail = request.form['contactEmail']
        inputSubject = request.form['subject']
        inputBody = request.form['bodyInput']
        inputAgree = int(request.form['contactAgree'])

        # Send Email
        sendEmail(inputName, inputSubject, inputEmail, inputBody)
        # Reply Email
        replyMessage(inputEmail, inputName)

        # Store details in database
        cur = mysql.connection.cursor()
        query = "INSERT INTO email_database (sender_name, sender_email, subject, body, check_policy, email_sent_on) VALUES(%s, %s, %s, %s, %s, %s)"
        result = cur.execute(query,(inputName, inputEmail, inputSubject, inputBody, bool(inputAgree), dt.now() ))
        mysql.connection.commit()
        cur.close()
        flash('Message sent successfully', 'success')
        return render_template('contact.html')
    return render_template('contact.html'), 200

    
# Route for login
@app.route('/login', methods=['GET', 'POST'])
@not_logged_in
def login():
    if request.method == "POST":
        # Get Login details
        user_id = request.form['idnumber']
        password_candidate = request.form['password']
        user = user_id.replace("'", "''")

            # Create cursor
        cur = mysql.connection.cursor()

        # Get user by user_id
        query = "SELECT * FROM user WHERE user_id = %(user_id)s"
        result = cur.execute(query, {'user_id': user})
        
        if result > 0:
            # Get only one row
            data = cur.fetchone()
            password = data['password']

            if sha256_crypt.verify(password_candidate, password):
                is_admin = data['is_admin']
                if bool(is_admin) == True:
                    session['logged_in'] = True
                    session['user_id'] = user
                    session['username'] = {'lname': data['last_name'],'fname': data['first_name']}
            
                    return "ADMIN PAGE"
                else:
                    session['logged_in'] = True
                    session['user_id'] = user
                    session['username'] = {'lname': data['last_name'],'fname': data['first_name']}
                
                    flash('Logged in successfully', 'success')
                    return redirect(url_for('user_dashboard'))
            else:
                flash('Incorrect password', 'danger')
                return render_template('login.html')
        else:
            flash('User account does not exist', 'danger')
            return render_template('login.html')

    return render_template('login.html'), 200

# Route for logout
@app.route('/logout', methods=['GET'])
@login_required
def logout():
    session.clear()
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))


# Route for dashboard
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def user_dashboard():
    if request.method == "POST":
        user_id = session['user_id']
        problem = request.form['issue']
        appointment_tag = randomDigits()
        input_date = request.form['inputDate']
        input_time = request.form['inputTime']
        terms = int(request.form['terms'])
        
        appoint = input_date + ' ' + input_time
        appointDate_Time = dt.strptime(appoint, '%Y-%m-%d %H:%M')
        

        cur = mysql.connection.cursor()
        query = "INSERT INTO appointment (user_id, problem, appointment_tag, appointDate_Time, terms) VALUES(%s, %s, %s, %s, %s)"
        result = cur.execute(query, (user_id, problem, appointment_tag, appointDate_Time, terms))
        # Commit cursor
        mysql.connection.commit()
        # Close Connection
        cur.close()
        flash('Appointment Booked', 'success')
        return redirect(url_for('user_dashboard'))
    return render_template('user_dashboard.html'), 200


# Route for appointment reservation
@app.route('/appointment_reserved', methods=['GET', 'POST'])
@login_required
def booking():
    cur = mysql.connection.cursor()
    query = "SELECT * FROM appointment WHERE user_id = %(id)s"
    result = cur.execute(query, {'id': session['user_id']})

    if result > 0:
        appointment = cur.fetchall()
        return render_template('appointment_reserved.html', appointment=appointment)
    else:
        msg = Markup("<h3>No Appointment Booked</h3>")
        return render_template('appointment_reserved.html', msg=msg)
    cur.close()
    return render_template('appointment_reserved.html')


# Edit Appointment
@app.route('/appointment_reserved/edit', methods=['GET', 'POST'])
@login_required
def edit():
    apptag = int(request.args['aptag'])

    if request.method == 'POST':
        problem = request.form['issue']
        input_date = request.form['inputDate']
        input_time = request.form['inputTime']

        appoint = input_date + ' ' + input_time
        appointDate_Time = dt.strptime(appoint, '%Y-%m-%d %H:%M')
        
        # Create Cursor
        cur = mysql.connection.cursor()             # Creates connection to mySQL database
        # Execute Query
        cur.execute("UPDATE appointment SET problem=%(issue)s, appointDate_Time=%(aptDT)s  WHERE appointment_tag=%(aptag)s", {'issue':problem, 'aptDT':appointDate_Time, 'aptag':apptag} ) 
        # Commit DB
        mysql.connection.commit()           # Sends changes to my_users table in the MYSQL database
        # Close Connection
        cur.close()

        flash('Appointment modified successfully.', 'success')

        return redirect(url_for('booking'))
    return render_template("edit_appointment.html")

# Cancel Appointment
@app.route('/appointment_reserved/cancel', methods=['GET'])
@login_required
def cancel():
    apptag = int(request.args['aptag'])
    # Create Cursor
    cur = mysql.connection.cursor() 
    query = "DELETE FROM appointment WHERE appointment_tag=%s"
    cur.execute(query, [apptag])
    # Commit DB
    mysql.connection.commit()           # Sends changes to appointment table in the MYSQL database
    # Close Connection
    cur.close()

    flash('Appointment cancelled.', 'success')

    return redirect(url_for('booking'))

# Route for changing password
@app.route('/setting/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangepswdForm(request.form)
    if request.method == "POST" and form.validate():
        user_id = session['user_id']
        _password = sha256_crypt.hash(str(form.new_password.data))
        # Store in database
        cur = mysql.connection.cursor()
        query = "UPDATE user SET password=%(pswd)s, account_modified_on=%(modify)s WHERE user_id=%(uid)s"
        cur.execute(query, {'pswd':_password, 'modify':dt.now(), 'uid':user_id})
        mysql.connection.commit()
        cur.close()
        # Clear session or logout since password has been changed
        session.clear()
        flash('Password changed. Please login with new password.', 'success')
        return redirect(url_for('login'))
    return render_template('change_password.html', form=form)

# Password Reset Codes
# Verify Email before sending token
@app.route('/request_email', methods=['GET', 'POST'])
@not_logged_in
def request_email():
    if request.method == 'POST':
        # Request email
        inputEmail = request.form['email']
        # Check if Email exist in user table
        cur = mysql.connection.cursor()
        query = "SELECT * FROM user WHERE (school_email=%(user_mail)s) OR (optional_email=%(user_mail)s)"
        result = cur.execute(query, {'user_mail':inputEmail})
        if result > 0:
            data = cur.fetchone()
            user_id = data['user_id']
            user_email = inputEmail
            user_fname = data['first_name']
            reset_password_link(user=user_id, email=user_email, username=user_fname)
            flash('Instructions to reset your password has been sent to your email.', 'info')
            return render_template('request_email.html') 
        else:
            flash('There is no account with this email. Please check if email is entered correctly.','danger')
            return render_template('request_email.html') 
        cur.close() 
    return render_template('request_email.html')


@app.route('/reset_password', methods=['GET', 'POST'])
@not_logged_in
def password_reset():
    token = request.args['token']
    result = TokenGEN.verify_reset_token(token)
    if result is None:
        flash("That is an invalid or expired token", 'warning')
        return redirect(url_for('request_email'))
    
    form = ChangepswdForm(request.form)
    if request.method == 'POST' and form.validate():
        userID = result["user_id"]
        _password = sha256_crypt.hash(str(form.new_password.data))
        # Store in database
        cur = mysql.connection.cursor()
        query = "UPDATE user SET password=%(pswd)s, account_modified_on=%(modify)s WHERE user_id=%(uid)s"
        cur.execute(query, {'pswd':_password, 'modify':dt.now(), 'uid':userID})
        mysql.connection.commit()
        cur.close()
        # Flash message
        flash('Password updated. Please login with new password.', 'success')
        return redirect(url_for('login'))
    return render_template('change_password.html', form=form)


# Route for editing user profile
app.add_url_rule("/settings/edit_profile", view_func=ProfileEndpoint.as_view("edit_profile"))