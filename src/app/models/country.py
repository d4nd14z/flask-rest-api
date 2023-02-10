from app.database import db, ma

class Country(db.Model):

    __tablename__ = "countries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    code = db.Column(db.String(5))
    flag = db.Column(db.String(255))

    def __init__(self, name, code, flag):
        self.name = name
        self.code = code
        self.flag = flag

    def __repr__(self):
        return f'<Country id: {self.id} / name: "{self.name}" />' 
    

class CountrySchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "code", "flag")


country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)
