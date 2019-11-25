# Local application imports
from content import mysql, mail, app
from .appoint_tag_gen import randomDigits
from .form import EditForm

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
    return render_template('appointment_reserved.html')


# Edit Article
@app.route('/edit', methods=['GET', 'POST'])
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

# Delete Article
@app.route('/cancel', methods=['GET'])
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

