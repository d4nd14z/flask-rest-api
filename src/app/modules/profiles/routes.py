from flask import request, jsonify
from app.modules.profiles import bp
from app.modules import tokenRequired
from app.database import db
from app.models.profile import Profile, profile_schema, profiles_schema

# Modelos adicionales para utilizar en consultas con JOIN
from app.models.user import User, user_schema, users_schema
from app.models.country import Country, country_schema, countries_schema

@bp.route("/", methods=["GET"])
@tokenRequired
def getProfilesAll(data):
    profiles = Profile.query.all()
    result = profiles_schema.dump(profiles)
    return profiles_schema.jsonify(result)


@bp.route("/<id>", methods=["GET"])
@tokenRequired
def getProfileById(data, id):
    profile = Profile.query.get(id)
    return profile_schema.jsonify(profile)


@bp.route("/", methods=["POST"])
@tokenRequired
def addProfile(data):
    avatar = request.json["avatar"] 
    genre = request.json["genre"]
    country = request.json["country"] 
    address = request.json["address"]
    phone = request.json["phone"]
    birthay_date = request.json["birthay_date"]
    user = request.json["user"]    
    profile = Profile(avatar, genre, country, address, phone, birthay_date, user)
    db.session.add(profile)
    db.session.commit()
    return profile_schema.jsonify(profile)


@bp.route("/<id>", methods=["PUT"])
@tokenRequired
def updateProfile(data, id):
    profile = Profile.query.get(id)
    profile.avatar = request.json["avatar"]
    profile.genre = request.json["genre"]
    profile.country = request.json["country"] 
    profile.address = request.json["address"]
    profile.phone = request.json["phone"]
    profile.birthay_date = request.json["birthay_date"]
    profile.user = request.json["user"]        
    db.session.commit()
    return profile_schema.jsonify(profile)


@bp.route("/<id>", methods=["DELETE"])
@tokenRequired
def deleteProfile(data, id):
    profile = Profile.query.get(id)
    db.session.delete(profile)
    db.session.commit()
    return profile_schema.jsonify(profile)


@bp.route("/full-profile/<id>", methods=["GET"])
@tokenRequired
def getFullProfile(data, id):
    results = db.session.query(Profile, User, Country).select_from(Profile).join(User, isouter=True).join(Country, isouter=True).filter(Profile.id == id).all()
    for profile, user, country in results:
        info = {
            "id": profile.id,
            "avatar": profile.avatar,
            "genre": profile.genre,
            "country": {
                "id": country.id,
                "name": country.name,
                "country": country.code,
                "flag": country.flag
            },
            "address": profile.address,
            "phone": profile.phone,
            "birthay_date": profile.birthay_date,
            "user": {
                "id": user.id,
                "fname": user.fname,
                "lname": user.lname,
                "email": user.email, 
                "login": user.login,
                "password": user.password
            }
        }
    return jsonify(info), 200  