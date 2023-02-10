from flask import request
from app.modules.countries import bp
from app.modules import tokenRequired
from app.database import db
from app.models.country import Country, country_schema, countries_schema

@bp.route("/", methods=["GET"])
@tokenRequired
def getCountriesAll(data):
    countries = Country.query.all()
    result = countries_schema.dump(countries)    
    return countries_schema.jsonify(result)


@bp.route("/<id>", methods=["GET"])
@tokenRequired
def getCountryById(data, id):
    country = Country.query.get(id)
    return country_schema.jsonify(country)


@bp.route("/", methods=["POST"])
@tokenRequired
def addCountry(data):
    info  = request.get_json()
    name = info["name"]
    code = info["code"]
    flag = info["flag"]
    country = Country(name, code, flag)
    db.session.add(country)
    db.session.commit()
    return country_schema.jsonify(country)


@bp.route("/<id>", methods=["PUT"])
@tokenRequired
def updateCountry(data, id):
    info = request.get_json()
    country = Country.query.get(id)
    country.name = info["name"]
    country.code = info["code"]
    country.flag = info["flag"]    
    db.session.commit()
    return country_schema.jsonify(country)


@bp.route("/<id>", methods=["DELETE"])
@tokenRequired
def deleteCountry(data, id):
    country = Country.query.get(id)
    db.session.delete(country)
    db.session.commit()
    return country_schema.jsonify(country)