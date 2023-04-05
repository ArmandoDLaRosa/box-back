from flask import Blueprint, request
from datetime import datetime
from ..extensions import db
from ..models.qual import Qual, QualSchema
import uuid
from flask_cors import cross_origin 
qual = Blueprint('qual', __name__)

@qual.route('/qual', methods = ['POST'])
@cross_origin()
def create_qual():
    timestamp = datetime.utcnow()
    body =  request.json        
    print(body)
    qual = Qual(match_id = body["match_id"], 
                       robot_id = body["robot_id"],                      
                       analysis = body["analysis"], 
                       created_at = timestamp, 
                       created_by = body["created_by"], 
                       updated_at = timestamp, 
                       updated_by = body["updated_by"], 
                       available=True)
    db.session.add(qual)
    db.session.commit()
    return QualSchema().dump(qual)

@qual.route('/qual/match/<match_id>/robot/<robot_id>', methods=['GET'])
@cross_origin()
def get_qual(match_id, robot_id):
    qual = Qual.query.get((match_id, robot_id))
    return QualSchema().dump(qual)

@qual.route('/qual', methods=['GET'])
@cross_origin()
def list_qual():
    quals = Qual.query.all()
    return  [QualSchema().dump(qual) for qual in quals]

@qual.route('/qual', methods=['PUT'])
@cross_origin()
def update_qual():
    timestamp = datetime.utcnow()
    body =  request.json    
    qual = Qual(robot_id = body["robot_id"],
                match_id = body["match_id"],
                analysis = body["analysis"], 
                created_at = datetime.strptime(body["created_at"], '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = body["created_by"], 
                updated_at = timestamp, 
                updated_by = body["updated_by"], 
                available = body["available"])
    db.session.merge(qual)
    db.session.commit()
    return  QualSchema().dump(qual)
    
@qual.route('/qual/match/<match_id>/robot/<robot_id>', methods=['DELETE'])    
@cross_origin()
def delete_qual(match_id, robot_id):
    qual = Qual.query.get((match_id, robot_id))
    db.session.delete(qual)
    db.session.commit()
    return QualSchema().dump(qual)
    