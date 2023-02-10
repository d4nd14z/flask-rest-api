from app.database import db, ma

class User(db.Model): 

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    login = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, fname, lname, email, login, password):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.login = login
        self.password = password

    def __repr__(self):
        return f'<Post "{self.fname} {self.lname} / {self.email}">'
    

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "fname", "lname", "email", "login", "password")

user_schema = UserSchema()
users_schema = UserSchema(many=True)