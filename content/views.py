# Local application imports
from content import mysql

# Third party imports
from flask.views import MethodView
from flask import render_template, request, redirect, url_for, flash, session
from functools import wraps

# Standard library import
from datetime import datetime as dt


# Login required
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, *kwargs)
        else:
            flash('Unauthorized Access, Please make sure you are logged in', 'danger')
            return redirect(url_for('login'))
    return wrap


# View for Index Route
class ProfileEndpoint(MethodView):
    @login_required
    # This function executes when request method for this route = get
    def get(self):
        user_id = session['user_id']
        cur = mysql.connection.cursor()
        query = "SELECT * FROM user WHERE user_id = %(user)s"
        result = cur.execute(query, {'user':user_id})
        data = cur.fetchone()
        dob = data['date_of_birth'].strftime('%Y-%m-%d')
        gender = data['gender']
        phone = data['phone_number']
        level = data['level']
        stud_email = data['school_email']
        opt_email = data['optional_email']
        act_creation = data['account_created_on'].strftime('%B %d, %Y')
        prog = data['programme']
        faculty = data['faculty_or_office']
        details = {'dob':dob, 'gender':gender, 'stud_email':stud_email,
                    'level':level, 'opt_email':opt_email, 'act_creation':act_creation,
                    'prog':prog, 'faculty':faculty, 'phone':phone
        }
        cur.close()
        return render_template('edit_profile.html', item=details)
        
    # This function executes when request method for this route = post
    def post(self):
        lname = request.form['edit_lname']
        fname = request.form['edit_fname']
        birth = request.form['edit_dob']
        schmail = request.form['edit_schmail']
        optmail = request.form['edit_optmail']
        ulevel = request.form['edit_level']
        ugender = request.form['edit_gender']
        uphone = request.form['edit_phone']
        uprog = request.form['edit_prog']
        ufaculty = request.form['edit_faculty']
        uid = session['user_id']
        act_modified = dt.now()

        cur = mysql.connection.cursor()
        query = "UPDATE user SET first_name=%s, last_name=%s, school_email=%s, gender=%s, phone_number=%s, date_of_birth=%s, level=%s, optional_email=%s,account_modified_on=%s, programme=%s, faculty_or_office=%s WHERE user_id=%s"
        cur.execute(query, (fname, lname, schmail, ugender, uphone, birth, ulevel, optmail, act_modified, uprog, ufaculty, uid))
        mysql.connection.commit()
        cur.close()
        # Flash message
        flash('User details have been updated.', 'success')

        return redirect(url_for('edit_profile'))
