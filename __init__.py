from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import cx_Oracle

db = SQLAlchemy()


def create_app():
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://BULLFLIX_PY:usf1956!@reade.forest.usf.edu:1521/cdb9'                                            
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://BULLFLIX_PY:usf1956!@reade.forest.usf.edu:1521/cdb9'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   
    #db = SQLAlchemy(app)
    db.init_app(app)       

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app