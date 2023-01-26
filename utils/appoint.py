from flask import Blueprint, url_for, render_template, redirect, request,flash,jsonify
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
import sqlalchemy
from utils.models import db, AppointmentsData
from pytz import timezone
import datetime

UTC = timezone('UTC')

def time_now():
    return datetime.now(UTC)


appointment = Blueprint('appointment', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(appointment)

@appointment.route('/appointment', methods=['GET', 'POST'])
def show():
    # if request.method == 'POST':
    if True ==True:
        pname = request.args.get('pname')
        age = request.args.get('age')
        gender = request.args.get('gender')
        med_comp = request.args.get('med_comp')
        address = request.args.get('address')
        height = request.args.get('height')
        weight = request.args.get('weight')
        dr_name = request.args.get('dr_name')
        app_date =datetime.datetime.strptime(request.args.get('app_date'), '%Y-%m-%d').date()
        app_time = datetime.datetime.strptime(request.args.get('app_time'), '%H:%M').time()
        print(10*"==")
        print(app_date,app_time)
        print(type(app_date),type(app_time))
        try:
            new_user = AppointmentsData(
                patient_name=pname,
                age=age,
                gender  = gender,
                med_comp = med_comp,
                address = address,
                height = height,
                weight = weight,
                dr_name=dr_name,
                app_date = app_date,
                app_time = app_time
            )

            db.session.add(new_user)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return redirect(url_for('register.show') + '?error=user-or-email-exists')

        appointment_id_from_db = AppointmentsData.query.filter_by(patient_name=pname).first().appointment_id

        
        appointment_reference ={}
        appointment_reference['id'] = appointment_id_from_db
        appointment_reference['pname'] = pname
        appointment_reference['doctor_name'] = dr_name
        appointment_reference['time'] = str(app_time)
        print(appointment_reference)
        # flash('Successfully booked appointment')
        return 'Appoinment has been fixed for {} at {} on {} with {}.<br> Appointment ID for reference is {}<br> Thank you'.format(pname,app_time,app_date,dr_name,appointment_id_from_db)