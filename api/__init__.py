from flask import Flask
from .extensions import db, ma, crs
from .routes.qual import qual
from .routes.quant import quant
from .routes.user import user

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://gxybdgkzxodngd:849b29123686ffba9dea3e30cd5b7fea68d1e659f6a3152e9d6b830c6188803c@ec2-3-230-24-12.compute-1.amazonaws.com:5432/d6egi1sged4ei0"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    db.init_app(app)
    ma.init_app(app)
    crs.init_app(app)
    
    app.register_blueprint(qual)
    app.register_blueprint(quant)
    app.register_blueprint(user)
    return app
