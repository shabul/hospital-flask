from flask import Blueprint, url_for, render_template, redirect, request, jsonify
from flask_login import LoginManager,login_required
from werkzeug.security import generate_password_hash
import pandas as pd


from utils.models import AppointmentsData,InPatientsData
from pytz import timezone
from datetime import datetime

UTC = timezone('UTC')

def time_now():
    return datetime.now(UTC)

def row2dict(row):
        d = {}
        for column in row.__table__.columns:
            d[column.name] = str(getattr(row, column.name))

        return d

dashboard = Blueprint('dashboard', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(dashboard)

@dashboard.route('/appoint_data', methods=['GET', 'POST'])
@login_required
def dashboard_appoint():
    print("Im in dashboard")
    inp_data = AppointmentsData.query.all()
    
    # print(inp_data,type(inp_data))
    
    

    response_inpatients = []
    for pat in inp_data:
        response_inpatients.append(row2dict(pat))

    
    return jsonify({'data' : response_inpatients})


@dashboard.route('/inpatient_data', methods=['GET', 'POST'])
def dashboard_inpatient():
    print("Im in dashboard")
    inp_data = InPatientsData.query.all()

    # print(inp_data,type(inp_data))
    
    

    response_inpatients = []
    for pat in inp_data:
        response_inpatients.append(row2dict(pat))

    # print(response_inpatients)
    
    return jsonify({'data' : response_inpatients})