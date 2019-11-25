# Standard library imports
import os

# Third party imports
from flask import Flask
from flask_mail import Mail
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from pathlib import Path

# Load .env file
load_dotenv(verbose=True)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Instantiate Flask
app = Flask(__name__)


# Config Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = str(os.getenv('MAIL_USERNAME'))
app.config['MAIL_PASSWORD'] = str(os.getenv('MAIL_PASSWORD'))
app.config['MAIL_MAX_EMAILS'] = 1000

mail = Mail(app)



# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = str(os.getenv('MYSQL_USER'))
app.config['MYSQL_PASSWORD'] = str(os.getenv('MYSQL_PASSWORD'))
app.config['MYSQL_DB'] = 'app'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Local application imports
from content import routes