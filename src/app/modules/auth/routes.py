import jwt
from jwt import exceptions
from datetime import datetime, timedelta
from flask import request, jsonify
from flask import current_app  # esto es igual a from app import app, pero no genera errores.
from app.modules.auth import bp

from app.models.user import User, user_schema, users_schema

@bp.route("/login", methods=["POST"])
def login():    
    data = request.get_json()
    user = User.query.filter_by(login=data["username"]).first()
    if user is not None:        
        if data["username"] == user.login and data["password"] == user.password:            
            token = jwt.encode({
                'user': data["username"],
                'expiration': str(datetime.now() + timedelta(seconds=120))                     
            }, current_app.config["SECRET_KEY"], algorithm="HS256")
            return jsonify({'token': token })
        else:                
            response = jsonify({"code": 404, "data":[], "message": "Authentication failed."})
            response.status_code = 404
            return response
    else:        
        response = jsonify({"code": 404, "data":[], "message": "Authentication failed."})
        response.status_code = 404
        return response