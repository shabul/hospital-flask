from flask import Blueprint, url_for, render_template, redirect, request
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

from utils.models import db, InPatients
from pytz import timezone
from datetime import datetime

UTC = timezone('UTC')

def time_now():
    return datetime.now(UTC)


dashboard = Blueprint('dashboard', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(dashboard)

@dashboard.route('/dashboard', methods=['GET', 'POST'])
def dashboard_api():
    
    inp_data = InPatients.query.all()

    print(inp_data,type(inp_data))

    for pat in inp_data:
        for p in pat:
            print(p)
    return str(inp_data)