from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# from flask_migrate import Migrate
# migrate = Migrate(app, db)


db = SQLAlchemy()
DB_NAME = "student"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # db.init_app(app)
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_service = os.getenv("DB_SERVICE")
    db_name = os.getenv("DB_NAME")

    # app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_password}@{db_service}/{db_name}"

    # 'mysql+pymysql://new-user:appleW00d@student-db-service/student-db'
    #db = SQLAlchemy(app)
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Errand

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all()
#         print('Created Database!')

def create_database(app):
    with app.app_context():
        if not path.exists('website/' + DB_NAME):
            db.create_all()
            print('Created Database!')