from ..extensions import db, ma
from datetime import datetime

class Pit(db.Model):
    # Each record is an analysis of a robot during match
    __tablename__ = 'pit_data'
    # ID    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # ATTRIBUTES    
    team_number = db.Column(db.String(50), nullable=False)
    team_name = db.Column(db.String(50), nullable=False)        
    data = db.Column(db.String(2000), nullable=False) # This is a json to keep flexible attributes
    # Standard attributes    
    created_at = db.Column(db.DateTime,  default=datetime.utcnow, nullable=False)
    created_by = db.Column(db.String(100), nullable=False)
    updated_at = db.Column(db.DateTime,  default=datetime.utcnow, nullable=False)
    updated_by = db.Column(db.String(100), nullable=False)
    available = db.Column(db.Boolean, nullable=False)      
    
class PitSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Pit

    # ID    
    id = ma.auto_field()
    # ATTRIBUTES    
    team_number = ma.auto_field()
    team_name = ma.auto_field()    
    data = ma.auto_field()
    # Standard attributes    
    created_at = ma.DateTime(format='%Y-%m-%d %H:%M:%S.%f')
    created_by = ma.auto_field()
    updated_at = ma.DateTime(format='%Y-%m-%d %H:%M:%S.%f')
    updated_by = ma.auto_field()
    available = ma.auto_field()
    
