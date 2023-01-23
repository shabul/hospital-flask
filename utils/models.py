from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String)



class Appointments(UserMixin,db.Model):
    appointment_id =db.Column(db.Integer, db.Sequence('seq_reg_id', start=1000, increment=1),primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    patient_name = db.Column(db.String(25))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    doctor_name = db.Column(db.String(25))
    date_time = db.Column(db.DateTime)

class InPatients(UserMixin,db.Model):
    patient_id =db.Column(db.Integer, db.Sequence('seq_reg_id', start=100, increment=1),primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    patient_name = db.Column(db.String(25))
    gender = db.Column(db.String(10))
    age = db.Column(db.String(4))
    doctor_name = db.Column(db.String(25))
    admit_time = db.Column(db.DateTime)
    fee_per_day = db.Column(db.Integer)




