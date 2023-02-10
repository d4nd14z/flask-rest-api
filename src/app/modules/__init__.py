import jwt
from flask import request, jsonify
from flask import current_app 
from datetime import datetime
from functools import wraps


""" Esta funcion - anotacion se utiliza para cuando se requiera que un EndPoint funcione con validacion de JWT Token
    Se utiliza la anotacion @tokenRequired sobre los EndPoints para utilizar la validacion
    @author: @d4nd14z
    @since: Feb 10 / 2023
"""
def tokenRequired(func):
    @wraps(func)
    def decorated(*args, **kwargs):        
        token = None                
        if "Authorization" in request.headers: 
            token = request.headers["Authorization"].split(" ")[1]            
        elif not token:
            return jsonify({"code": 401, "data":[], "message": "Invalid Token."}), 401
       
        try: 
            data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])         
            expdate = datetime.strptime(data["expiration"][:-7], "%Y-%m-%d %H:%M:%S")            
            if (datetime.now() > expdate):
                raise jwt.ExpiredSignatureError
        except jwt.DecodeError:
            return jsonify({"code": 401, "data":[], "message": "Invalid Token."}), 401         
        except jwt.ExpiredSignatureError:
            return jsonify({"code": 408, "data":[], "message": "Expired Token."}), 408       
        except Exception as ex:
            return jsonify({"code": 500, "data":[], "message": f"Internal Error: {str(ex)}"}), 500                   
            
        return func(data, *args, **kwargs)
    return decorated