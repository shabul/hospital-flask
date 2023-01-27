from flask import Blueprint, url_for, render_template, redirect, request,jsonify
from flask_login import LoginManager, login_user,login_required
from werkzeug.security import check_password_hash

from utils.models import db, Users

login = Blueprint('login', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(login)

@login.route('/login', methods=['GET', 'POST'])
def show():
    if True:
        username = request.args.get('username')
        password = request.args.get('password')
        print(username,password,"in function")
        user = Users.query.filter_by(username=username).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                print("logged in")
                return jsonify({"auth" : "success"})
            else:
                return jsonify({"auth":"Incorrect Username / Password"})
                # return redirect(url_for('login.show') + '?error=incorrect-password')
        else:
            return jsonify({"auth":"User not found. Kindly Register"})
            # return redirect(url_for('login.show') + '?error=user-not-found')
    else:
        return render_template('login.html')
