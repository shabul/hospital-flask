from flask import Blueprint, url_for, redirect,render_template
from flask_login import LoginManager, login_required, logout_user

logout = Blueprint('logout', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(logout)

@logout.route('/logout')
@login_required
def show():
    logout_user()
    return render_template('login.html')