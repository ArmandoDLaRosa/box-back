from ..extensions import db, ma
from datetime import datetime

class Qual(db.Model):
    # Each record is an analysis of a robot during match
    __tablename__ = 'qualitative_analysis'
    # ID    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # ATTRIBUTES    
    match_id = db.Column(db.String(50), nullable=False)
    robot_id = db.Column(db.String(50), nullable=False)        
    analysis = db.Column(db.String(2000), nullable=False) # This is a json to keep flexible attributes
    # Standard attributes    
    created_at = db.Column(db.DateTime,  default=datetime.utcnow, nullable=False)
    created_by = db.Column(db.String(100), nullable=False)
    updated_at = db.Column(db.DateTime,  default=datetime.utcnow, nullable=False)
    updated_by = db.Column(db.String(100), nullable=False)
    available = db.Column(db.Boolean, nullable=False)      
    
class QualSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Qual

    # ID    
    id = ma.auto_field()
    # ATTRIBUTES    
    match_id = ma.auto_field()
    robot_id = ma.auto_field()    
    analysis = ma.auto_field()
    # Standard attributes    
    created_at = ma.DateTime(format='%Y-%m-%d %H:%M:%S.%f')
    created_by = ma.auto_field()
    updated_at = ma.DateTime(format='%Y-%m-%d %H:%M:%S.%f')
    updated_by = ma.auto_field()
    available = ma.auto_field()
    
