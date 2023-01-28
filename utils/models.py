from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String)



# class Appointments(UserMixin,db.Model):
#     appointment_id =db.Column(db.Integer, db.Sequence('seq_reg_id', start=1000, increment=1),primary_key=True)
#     created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
#     patient_name = db.Column(db.String(25))
#     age = db.Column(db.Integer)
#     gender = db.Column(db.String(10))
#     med_comp = db.Column(db.String(100))
#     address = db.Column(db.String(100))
#     height = db.Column(db.Integer)
#     weight = db.Column(db.Integer)
#     dr_name = db.Column(db.String(25))
#     app_date = db.Column(db.Date)
#     app_time = db.Column(db.Time)

# class InPatients(UserMixin,db.Model):
#     patient_id =db.Column(db.Integer, db.Sequence('seq_reg_id', start=100, increment=1),primary_key=True)
#     created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
#     patient_name = db.Column(db.String(25))
#     gender = db.Column(db.String(10))
#     age = db.Column(db.String(4))
#     doctor_name = db.Column(db.String(25))
#     admit_time = db.Column(db.DateTime)
#     fee_per_day = db.Column(db.Integer)

class AppointmentsData(UserMixin,db.Model):
    appointment_id =db.Column(db.Integer, db.Sequence('seq_reg_id', start=1000, increment=1),primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    patient_name = db.Column(db.String(25))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    med_comp = db.Column(db.String(100))
    address = db.Column(db.String(100))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    dr_name = db.Column(db.String(25))
    app_date = db.Column(db.Date)
    app_time = db.Column(db.Time)
    

class InPatientsData(UserMixin,db.Model):
    patient_id =db.Column(db.Integer, db.Sequence('seq_reg_id', start=100, increment=1),primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    patient_name = db.Column(db.String(25))
    dob = db.Column(db.Date)
    gender = db.Column(db.String(10))
    room_type = db.Column(db.String(25))
    insurance = db.Column(db.Boolean)
    emp_type = db.Column(db.String(20))
    contact_person = db.Column(db.String(40))
    phone_number = db.Column(db.String(20))
    dr_name = db.Column(db.String(25))
    admit_date = db.Column(db.Date)
    admit_time = db.Column(db.Time)
    minor = db.Column(db.Boolean)
    accident = db.Column(db.Boolean)



## Age =- PIE chart
## Inpatient - Count - 2 cards

## docotr and his appoitments - bar chart - count of appoitments

