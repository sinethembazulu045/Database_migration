from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:pass@127.0.0.1/development'
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager =  Manager(app)

manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    recruit = db.relationship('Recruit', backref='owner', lazy='dynamic')

class Recriut (db.Model):
    id = db.Column(db.Integer, primary_key =True)
    first_name = db.Column(db.String(20))
    surname = db.Column(db.String(20))
    rocketchat_user = db.Column(db.String(100))
    github_name = db.Column(db.String(80))
    id_number =db.Column(db.Integer)
    personal_email_address =db.Column(db.VARCHAR(100), unique =True)
    cohort_recruit = db.Column(db.VARCHAR(100))

if __name__== '__main__':
    manager.run()