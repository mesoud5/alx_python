from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import re
import sys
from sqlalchemy import create_engine, column, Integer, String
from sqlalchemy.orm import sessionmaker
# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)

############################# TO DO 1 ############################
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqldb://{db_username}:{db_password}@localhost:3306/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print("MySQL URI:", "mysql://" + app.config['SQLALCHEMY_DATABASE_URI']) 
###############################################################
db = SQLAlchemy(app)

############################  TO DO 2 ##############################
class user(db.Model):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(265))
    email = db.Column(String(265), unique=True, nullable=False)
#################################################################

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This calls the function to create tables


@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)