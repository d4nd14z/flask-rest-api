from app.database import db, ma

class Profile(db.Model):

    __tablename__ = "profiles"
    id = db.Column(db.Integer, primary_key=True)    
    avatar = db.Column(db.String(255))        
    genre = db.Column(db.String(1)) #('M','F','N')    
    country = db.Column(db.Integer, db.ForeignKey('countries.id', ondelete='CASCADE'), nullable=False)
    address = db.Column(db.String(255))
    phone = db.Column(db.String(50))
    birthay_date = db.Column(db.DateTime, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, avatar, genre, country, address, phone, birthay_date, user):
        self.avatar = avatar
        self.genre = genre
        self.country = country
        self.address = address
        self.phone = phone
        self.birthay_date = birthay_date
        self.user = user

    def __repr__(self):
        return f'<Profile "{ self.id }" />'
    

class ProfileSchema(ma.Schema):
    class Meta:
        fields = ("id", "avatar", "genre", "country", "address", "phone", "birthay_date", "user")
    
profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)
