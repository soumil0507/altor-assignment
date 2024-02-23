from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import environ, getcwd, path

load_dotenv(path.join(getcwd(), '.env'))

DB_URI = environ.get('DB_URI')
ASSIGNMENT_DATA_URI = environ.get('ASSIGNMENT_DATA_URI')

db = SQLAlchemy()