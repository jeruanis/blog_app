
from http import server
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, user_loaded_from_request
from flask_mail import Mail
from app.config import Config

#remove the parameter as it will be put inside the creation function
db = SQLAlchemy() 
bcrypt = Bcrypt() 
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail() 

def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from app.users.routes import users #importing the instance of Blueprint
    from app.posts.routes import posts
    from app.main.routes import main
    from app.errors.handlers import errors #importing the instance of the errors Blueprint
    app.register_blueprint(users) #registering the user blueprint
    app.register_blueprint(posts) 
    app.register_blueprint(main) 
    app.register_blueprint(errors) 

    return app
