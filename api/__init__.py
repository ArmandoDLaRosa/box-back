from flask import Flask
from .extensions import db, ma, crs
from .routes.qual import qual
from .routes.quant import quant
from .routes.user import user

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:01570376@192.168.3.35:5432/thebox"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    db.init_app(app)
    ma.init_app(app)
    crs.init_app(app)
    
    app.register_blueprint(qual)
    app.register_blueprint(quant)
    app.register_blueprint(user)
    return app
