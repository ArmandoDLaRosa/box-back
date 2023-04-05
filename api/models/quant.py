from ..extensions import db, ma
from datetime import datetime

class Quant(db.Model):
    # Each record is a robot's stats of a match
    __tablename__ = 'quantitative_analysis'
    # ID    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # ATTRIBUTES    
    match_id = db.Column(db.String(50), nullable=False)
    robot_id = db.Column(db.String(50), nullable=False)        
    stats = db.Column(db.String(1000), nullable=False) # This is a json to keep flexible attributes
    # Standard attributes    
    created_at = db.Column(db.DateTime,  default=datetime.utcnow, nullable=False)
    created_by = db.Column(db.String(100), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_by = db.Column(db.String(100), nullable=False)
    available = db.Column(db.Boolean, nullable=False)      
    
class QuantSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Quant

    # ID    
    id = ma.auto_field()
    # ATTRIBUTES    
    match_id = ma.auto_field()
    robot_id = ma.auto_field()    
    stats = ma.auto_field()
    # Standard attributes    
    created_at = ma.DateTime(format='%Y-%m-%d %H:%M:%S.%f')
    created_by = ma.auto_field()
    updated_at = ma.DateTime(format='%Y-%m-%d %H:%M:%S.%f')
    updated_by = ma.auto_field()
    available = ma.auto_field()    