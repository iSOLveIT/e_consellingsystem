from wtforms import validators, SelectField, Form
from wtforms.fields.html5 import DateField, TimeField

# Form Class for Users Registration
class EditForm(Form):
    options = [('Academic/Career', 'Academic/Career'),('Personal/Social', 'Persornal/Social'),('Financial', 'Financial'),('Health', 'Health'),('Others', 'Others')]
    issue = SelectField('Type of Issue', choices=options, validators=[validators.InputRequired()])
    inputTime = TimeField('Appointment Time', validators=[validators.InputRequired()], format='%H:%M %p')
    inputDate = DateField('Appointment Date', validators=[validators.InputRequired()], format='%Y-%m-%d')
