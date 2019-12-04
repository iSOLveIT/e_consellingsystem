# Local application imports

# Third party imports
from flask_wtf import FlaskForm
from wtforms import PasswordField, validators

# Standard library import

class ChangepswdForm(FlaskForm):
    new_password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.InputRequired(message="Please enter your new password"),
        validators.Length(min=8),
        validators.EqualTo('confirm_password', message='Passwords do not match.')
    ])
    confirm_password = PasswordField('Confirm Password', [
        validators.DataRequired(),
        validators.InputRequired()
    ])
