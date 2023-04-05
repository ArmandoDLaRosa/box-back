from flask import Blueprint, request
from datetime import datetime
from ..extensions import db
from flask_cors import cross_origin 
from ..models.user import User, UserSchema

import uuid
import json 

user = Blueprint('user', __name__)

@user.route('/user', methods=['POST'])
@cross_origin()
def create_user():
    timestamp = datetime.utcnow()
    body =  request.json
    user = User(id = str(uuid.uuid4()),
                name = body["name"], 
                email = body["email"], 
                created_at = timestamp, 
                created_by = body["created_by"], 
                updated_at = timestamp, 
                updated_by = body["updated_by"], 
                available = body["available"])
    db.session.add(user)
    db.session.commit()
    return UserSchema().dump(user)

@user.route('/user/<id>', methods=['GET'])
@cross_origin()
def get_user(id):
    user = User.query.get(id)
    return  UserSchema().dump(user)

@user.route('/user', methods=['GET'])
@cross_origin()
def list_user():
   users = User.query.all()
   return  [UserSchema().dump(user) for user in users]

@user.route('/user', methods=['PUT'])
@cross_origin()
def update_user():
    timestamp = datetime.utcnow()
    body =  request.json    
    user = User(id = body["id"],
                name = body["name"], 
                email = body["email"], 
                created_at = datetime.strptime(body["created_at"], '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = body["created_by"], 
                updated_at = timestamp, 
                updated_by = body["updated_by"], 
                available = body["available"])
    db.session.merge(user)
    db.session.commit()
    return  UserSchema().dump(user)

@user.route('/user/<id>', methods=['DELETE'])  
@cross_origin()  
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return UserSchema().dump(user)
    