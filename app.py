from flask import Flask,render_template
import sqlalchemy
from flask_login import LoginManager,login_required

from utils.models import db, Users

from utils.index import index
from utils.login import login
from utils.logout import logout
from utils.register import register
from utils.home import home
from utils.appoint import appointment
from utils.inpatient import inpatient
from utils.dashboard import dashboard

## https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login -- ref



app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'

login_manager = LoginManager()
login_manager.init_app(app)
db.init_app(app)
app.app_context().push()

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(register)
app.register_blueprint(home)
app.register_blueprint(appointment)
app.register_blueprint(inpatient)
app.register_blueprint(dashboard)





@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/book_appointment')
@login_required
def appoint():
    return render_template('appointment.html')


@app.route('/inpatient_entry')
@login_required
def inpatient():
    return render_template('inpatient.html')


@app.route('/view_dashboard')
@login_required
def dash_page():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
