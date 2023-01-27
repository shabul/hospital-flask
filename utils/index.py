from flask import Blueprint, redirect,render_template

index = Blueprint('index', __name__, template_folder='../templates')

@index.route('/', methods=['GET'])
def show():
    return render_template('login.html')