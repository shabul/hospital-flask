from flask import Blueprint, url_for, render_template, redirect, request, jsonify
from flask_login import LoginManager,login_required
from werkzeug.security import generate_password_hash
import pandas as pd
from collections import Counter


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

stats = Blueprint('stats', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(stats)

@stats.route('/stats_data', methods=['GET', 'POST'])
@login_required
def stats_appoint():
    print("Im in stats")
    app_data = AppointmentsData.query.all()
    
    # print(inp_data,type(inp_data))
    
    

    response_app_data = []
    for pat in app_data:
        response_app_data.append(row2dict(pat))

    app_data = pd.DataFrame(response_app_data)



    gender_pie_chart = {
        'labels' : list(app_data.gender.value_counts().to_dict().keys()),
        'values' : list(app_data.gender.value_counts().to_dict().values())
    }
    dis_data = Counter([item for sublist in  [val.split(',') for val in app_data['med_comp'].values]  for item in sublist])
    dis_bar_chart = {
        'labels' : list(dis_data.keys()),
        'values' : list(dis_data.values())
        
    }

    dr_pie_chart = {
                "labels" : list(app_data.dr_name.value_counts().to_dict().keys()),
                "values" : list(app_data.dr_name.value_counts().to_dict().values()),
            }

    #-----------------
    week = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}


    x = lambda date : week[datetime.strptime(date,"%Y-%m-%d").date().weekday()]

    app_data['weekday'] = app_data['app_date'].apply(x)

    

    week_bar_chart = {
        'labels' : list(app_data.weekday.value_counts().to_dict().keys()),
        'values' : list(app_data.weekday.value_counts().to_dict().values())
        
    }
    




    return jsonify({'data' : {
        "gender_chart" : gender_pie_chart,
        'dis_bar_chart' : dis_bar_chart,
        'dr_pie_chart' : dr_pie_chart,
        'week_bar_chart' : week_bar_chart


    }})


# @dashboard.route('/inpatient_data', methods=['GET', 'POST'])
# def dashboard_inpatient():
#     print("Im in dashboard")
#     inp_data = InPatientsData.query.all()

#     # print(inp_data,type(inp_data))
    
    

#     response_inpatients = []
#     for pat in inp_data:
#         response_inpatients.append(row2dict(pat))

#     # print(response_inpatients)
    
#     return jsonify({'data' : response_inpatients})