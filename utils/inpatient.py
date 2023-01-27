from flask import Blueprint, url_for, render_template, redirect, request
from flask_login import LoginManager,login_required
from werkzeug.security import generate_password_hash
import sqlalchemy
from utils.models import db, InPatientsData
from pytz import timezone
from datetime import datetime

UTC = timezone('UTC')

def time_now():
    return datetime.now(UTC)


inpatient = Blueprint('inpatient', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(inpatient)

@inpatient.route('/inpatient', methods=['GET', 'POST'])
@login_required
def show():
    if True:
        print(1000*"_+_+")
        x = request.args.get('res')
        print(x)
        patient_name  = 'shssssgsj'   
        dob  = datetime.strptime('2022-09-12', '%Y-%m-%d').date()  
        gender  =   'Male'  
        room_type  =  'AC'   
        insurance  =  True   
        emp_type  =    'Givt' 
        contact_person  =  'shasssb'   
        phone_number  =   '7897'  
        dr_name  =   'jhghjfd'  
        admit_date  =  datetime.strptime('2022-05-06', '%Y-%m-%d').date()  
        admit_time  =  datetime.strptime('23:47', '%H:%M').time()   
        minor  =  True   
        accident  =  False   
        print(10*"==")
        print(admit_date,admit_time)
        print(type(admit_date),type(admit_time))

        try:
            new_user = InPatientsData(
                patient_name  =patient_name     ,
                dob  = dob    ,
                gender  = gender    ,
                room_type  = room_type    ,
                insurance  =    insurance ,
                emp_type  =    emp_type ,
                contact_person  = contact_person    ,
                phone_number  =     phone_number,
                dr_name  =  dr_name   ,
                admit_date  =   admit_date  ,
                admit_time  = admit_time    ,
                minor  =    minor ,
                accident  =  accident   ,
            )

            db.session.add(new_user)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return 'Entered Data Already exists or mismatches with the format it takes.<br> Kindly Re-check all fields and Book again.'

        inpatient_id_from_db = InPatientsData.query.filter_by(patient_name=patient_name).first().patient_id

        
        inpatient_reference ={}
        inpatient_reference['id'] = inpatient_id_from_db
        # appointment_reference['pname'] = pname
        # appointment_reference['doctor_name'] = doctorname
        # appointment_reference['time'] = date_time_appoinement
        print(inpatient_reference)

        # flash("Added Successfully")
        return 'Inpatient Data has been entered for {} at {} on {} with {}.<br> Inpataient ID for reference is {}<br> Thank you'.format(patient_name,admit_time,admit_date,dr_name,inpatient_id_from_db)