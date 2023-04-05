from flask import Blueprint, request
from datetime import datetime
from ..extensions import db
from flask_cors import cross_origin 
from ..models.quant import Quant, QuantSchema
import uuid

quant = Blueprint('quant', __name__)

@quant.route('/quant', methods = ['POST'])
@cross_origin()
def create_quant():
    timestamp = datetime.utcnow()
    body =  request.json    
    quant = Quant(robot_id = str(uuid.uuid4()), 
                        match_id = str(uuid.uuid4()), 
                        stats = body["stats"], 
                        created_at = timestamp, 
                        created_by = body["created_by"], 
                        updated_at = timestamp, 
                        updated_by = body["updated_by"], 
                        available=True)
    db.session.add(quant)
    db.session.commit()
    return QuantSchema().dump(quant)

@quant.route('/quant/match/<match_id>/robot/<robot_id>', methods=['GET'])
@cross_origin()
def get_quant(match_id, robot_id):
    quant = Quant.query.get((match_id, robot_id))
    return  QuantSchema().dump(quant)

@quant.route('/quant', methods=['GET'])
@cross_origin()
def list_quant():
    quants = Quant.query.all()
    return  [QuantSchema().dump(quant) for quant in quants]
    
@quant.route('/quant', methods=['PUT'])
@cross_origin()
def update_quant():
    timestamp = datetime.utcnow()
    body =  request.json    
    quant = Quant(robot_id = body["robot_id"],
                 match_id = body["match_id"],
                stats = body["stats"], 
                created_at = datetime.strptime(body["created_at"], '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = body["created_by"], 
                updated_at = timestamp, 
                updated_by = body["updated_by"], 
                available = body["available"])
    db.session.merge(quant)
    db.session.commit()
    return  QuantSchema().dump(quant)

@quant.route('/quant/match/<match_id>/robot/<robot_id>', methods=['DELETE'])   
@cross_origin() 
def delete_quant(match_id, robot_id):
    quant = Quant.query.get((match_id, robot_id))
    db.session.delete(quant)
    db.session.commit()
    return QuantSchema().dump(quant)
