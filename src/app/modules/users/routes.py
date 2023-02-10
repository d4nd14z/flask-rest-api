from flask import request
from app.modules.users import bp
from app.modules import tokenRequired
from app.database import db
from app.models.user import User, user_schema, users_schema

@bp.route("/", methods=["GET"])
@tokenRequired
def getUsersAll(data):
    users = User.query.all()
    result = users_schema.dump(users)
    return users_schema.jsonify(result) 


@bp.route("/<id>", methods=["GET"])   
@tokenRequired
def getUsersById(data, id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


@bp.route("/", methods=["POST"])
@tokenRequired
def insertUser(data):
    info = request.get_json()
    user = User(info["fname"], info["lname"], info["email"], info["login"], info["password"])
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user)


@bp.route("/<id>", methods=["PUT"])
@tokenRequired
def updateUser(data, id):
    info = request.get_json()
    user = User.query.get(id)  
    user.fname = info["fname"]  
    user.lname = info["lname"]
    user.email = info["email"]
    user.login = info["login"]
    user.password = info["password"]
    db.session.commit()
    return user_schema.jsonify(user)
    

@bp.route("/<id>", methods=["DELETE"])
@tokenRequired
def deleteUser(data, id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)

