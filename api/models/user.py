from ..extensions import db, ma
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    # ID
    id = db.Column(db.String(50), primary_key=True)
    # ATTRIBUTES
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    # Standard attributes
    created_at = db.Column(db.DateTime,  default=datetime.utcnow, nullable=False)
    created_by = db.Column(db.String(100), nullable=False)
    updated_at = db.Column(db.DateTime,  default=datetime.utcnow, nullable=False)
    updated_by = db.Column(db.String(100), nullable=False)
    available = db.Column(db.Boolean, nullable=False)     
    
class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    # ID    
    id = ma.auto_field()
    # ATTRIBUTES    
    name = ma.auto_field()
    email = ma.auto_field()    
    # Standard attributes    
    created_at = ma.DateTime(format='%Y-%m-%d %H:%M:%S.%f')
    created_by = ma.auto_field()
    updated_at = ma.DateTime(format='%Y-%m-%d %H:%M:%S.%f')
    updated_by = ma.auto_field()
    available = ma.auto_field()    
    