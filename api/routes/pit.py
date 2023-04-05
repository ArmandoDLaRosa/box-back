from flask import Blueprint, request
from datetime import datetime
from ..extensions import db
from ..models.pit import Pit, PitSchema
import uuid
from flask_cors import cross_origin 
pit = Blueprint('pit', __name__)

@pit.route('/pit', methods = ['POST'])
@cross_origin()
def create_pit():
    timestamp = datetime.utcnow()
    body =  request.json        
    pit = Pit(team_number = body["team_number"], 
                       team_name = body["team_name"],                      
                       data = body["data"], 
                       created_at = timestamp, 
                       created_by = body["created_by"], 
                       updated_at = timestamp, 
                       updated_by = body["updated_by"], 
                       available=True)
    db.session.add(pit)
    db.session.commit()
    return PitSchema().dump(pit)

@pit.route('/pit/tean/<team_number>/robot/<robot_id>', methods=['GET'])
@cross_origin()
def get_pit(match_id, robot_id):
    pit = Pit.query.get((match_id, robot_id))
    return PitSchema().dump(pit)

@pit.route('/pit', methods=['GET'])
@cross_origin()
def list_pit():
    pits = Pit.query.all()
    return  [PitSchema().dump(pit) for pit in pits]

@pit.route('/pit', methods=['PUT'])
@cross_origin()
def update_pit():
    timestamp = datetime.utcnow()
    body =  request.json    
    pit = Pit(robot_id = body["robot_id"],
                match_id = body["match_id"],
                analysis = body["analysis"], 
                created_at = datetime.strptime(body["created_at"], '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = body["created_by"], 
                updated_at = timestamp, 
                updated_by = body["updated_by"], 
                available = body["available"])
    db.session.merge(pit)
    db.session.commit()
    return  PitSchema().dump(pit)
    
@pit.route('/pit/match/<match_id>/robot/<robot_id>', methods=['DELETE'])    
@cross_origin()
def delete_pit(match_id, robot_id):
    pit = Pit.query.get((match_id, robot_id))
    db.session.delete(pit)
    db.session.commit()
    return PitSchema().dump(pit)
    