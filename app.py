from flask import Flask
import sqlalchemy
from flask_login import LoginManager

from utils.models import db, Users

from utils.index import index
from utils.login import login
from utils.logout import logout
from utils.register import register
from utils.home import home

app = Flask(__name__, static_folder='../templates/static')

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

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)
