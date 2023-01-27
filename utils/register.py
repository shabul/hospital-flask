from flask import Blueprint, url_for, render_template, redirect, request,jsonify
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
import sqlalchemy
from utils.models import db, Users

register = Blueprint('register', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(register)

@register.route('/register', methods=['GET', 'POST'])
def show():
    if True:
        username = request.args.get('username')
        email = request.args.get('email')
        password = request.args.get('password')
        confirm_password = request.args.get('confirm_password')
        
        print("I am in register page")
        print(username,email,password,confirm_password)
        
        if username and email and password and confirm_password:
            if password == confirm_password:
                hashed_password = generate_password_hash(
                    password, method='sha256')
                try:
                    new_user = Users(
                        username=username,
                        email=email,
                        password=hashed_password,
                    )

                    db.session.add(new_user)
                    db.session.commit()
                    print('Success Registaion')
                    print("jsonify({'registration' : 'success'})")
                    return jsonify({'registration' : 'success'})
                
                except sqlalchemy.exc.IntegrityError:
                    print("jsonify({'registration' : 'User or Email already exists.'})")
                    return jsonify({'registration' : 'User or Email already exists.'})
                
                

            else:
                ## PAssword doesnt match
                print("jsonify({'registration' : 'Password Mismatch'})")
                return jsonify({'registration' : 'Password Mismatch'})
                
                
        else:
            print("jsonify({'registration' : 'Please fill all the fields'})")
            return jsonify({'registration' : 'Please fill all the fields'})
                    