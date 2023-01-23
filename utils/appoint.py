from flask import Blueprint, url_for, render_template, redirect, request
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

from utils.models import db, Appointments
from pytz import timezone
from datetime import datetime

UTC = timezone('UTC')

def time_now():
    return datetime.now(UTC)


appointment = Blueprint('appointment', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(appointment)

@appointment.route('/appointment', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        pname = request.form['pname']
        age_input = request.form['age']
        doctorname = request.form['doctorname']
        
        gender_input = "M"
        date_time_appoinement = time_now()
        try:
            new_user = Appointments(
                patient_name=pname,
                age=age_input,
                gender  = gender_input,
                doctor_name=doctorname,
                date_time = date_time_appoinement
            )

            db.session.add(new_user)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return redirect(url_for('register.show') + '?error=user-or-email-exists')

        appointment_id_from_db = Appointments.query.filter_by(patient_name=pname).first().appointment_id

        
        appointment_reference ={}
        appointment_reference['id'] = appointment_id_from_db
        appointment_reference['pname'] = pname
        appointment_reference['doctor_name'] = doctorname
        appointment_reference['time'] = date_time_appoinement
        return appointment_reference