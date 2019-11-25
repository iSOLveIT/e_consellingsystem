# Local application imports
from content import mysql, mail
from .token import TokenGEN


# Third party imports
from flask_mail import Message
from flask import url_for, Markup


# Standard library import
from datetime import datetime as dt


def sendEmail(_name, _subject, _email, _body):
    # SEND EMAIL
    _recipient = 'isolveitgroup@gmail.com'
    msg = Message(_subject, sender=('COUNSELLING & GENDER UNIT', 'isolveitgroup@gmail.com'), recipients=[_recipient])
    assert msg.sender == "COUNSELLING & GENDER UNIT <isolveitgroup@gmail.com>"
    msg.body = f'''{_body}


Sender's Name: {_name}
Sender's Email: {_email}
Date Sent:  {dt.now().strftime('%B %d, %Y, %H:%M ') + 'GMT'}
'''
    mail.send(msg)
    return 'OK'


def replyMessage(_email, _senderName):
    # REPLY EMAIL
    _subj = 'Message Received'
    mesg = Message(_subj, sender=('COUNSELLING & GENDER UNIT', 'isolveitgroup@gmail.com'), recipients=[_email])
    assert mesg.sender == "COUNSELLING & GENDER UNIT <isolveitgroup@gmail.com>"
    mesg.body = f'''Hello {_senderName},
The message you sent to the COUNSELLING & GENDER UNIT has been received. The unit will contact you within 24 hours.
Thank you.

Regards,
COUNSELLING & GENDER UNIT

Date Sent:  {dt.now().strftime('%B %d, %Y, %H:%M ') + 'GMT'}
'''
    mail.send(mesg)
    return 'OK'


def reset_password_link(user, email, username):
    user_id = user
    email_address = email
    name = username
    Edate = dt.now()
    token = TokenGEN.get_reset_token(user_id=str(user_id))
    subj = 'Password Reset Requested'
    msg = Message(subj, sender=('COUNSELLING & GENDER UNIT', 'isolveitgroup@gmail.com'), recipients=[email_address])
    assert msg.sender == "COUNSELLING & GENDER UNIT <isolveitgroup@gmail.com>"
    
    msg.body = "<h2 style='text-align: center;'>Password Reset Instructions</h2> <br> <br> A password reset event have been requested by you on %s (GMT). <br><br> Please note that the password reset window is limited to one hour. If you do not reset your password within one hour, you will need to submit a new request. <br><br> To complete the password reset process, visit the following link: <br> <a href='http://127.0.0.1:4000/reset_password?token=%s'>Click here to reset password</a> <br><br> <b>Don't recognize this activity?</b> <br> Ignore this email and no changes will be made to your account.<br><br> The Counselling and Gender Unit" %(Edate.strftime('%A, %B %d, %Y %I:%M %p'), token)
    msg.html = msg.body
    
    mail.send(msg)
    return 'OK'