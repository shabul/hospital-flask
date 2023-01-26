from flask import Blueprint, url_for, render_template, redirect, request
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

from utils.models import db, InPatients
from pytz import timezone
from datetime import datetime

UTC = timezone('UTC')

def time_now():
    return datetime.now(UTC)


inpatient = Blueprint('inpatient', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(inpatient)

@inpatient.route('/inpatient', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        pname = request.form['inpname']
        age_input = request.form['inpage']
        doctorname = request.form['admit_time']
        
        gender_input = "M"
        date_time_appoinement = time_now()
        fee_per_day_input = 1000
        try:
            new_user = InPatients(
                patient_name=pname,
                age=age_input,
                gender  = gender_input,
                doctor_name=doctorname,
                admit_time = date_time_appoinement,
                fee_per_day = fee_per_day_input
            )

            db.session.add(new_user)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return redirect(url_for('register.show') + '?error=user-or-email-exists')

        appointment_id_from_db = InPatients.query.filter_by(patient_name=pname).first().patient_id

        
        appointment_reference ={}
        appointment_reference['id'] = appointment_id_from_db
        appointment_reference['pname'] = pname
        appointment_reference['doctor_name'] = doctorname
        appointment_reference['time'] = date_time_appoinement
        print(appointment_reference)

        # flash("Added Successfully")
        return render_template('inpatient.html')