from flask import Flask
from config import Config
from app.database import db, ma

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    #Initialize Flask extensions here
    db.init_app(app)
    ma.init_app(ma)
    with app.app_context():
        db.create_all()

    #Register Blueprints here
    from app.modules.auth import bp as authBP
    app.register_blueprint(authBP)
    from app.modules.users import bp as usersBP
    app.register_blueprint(usersBP, url_prefix="/users")
    from app.modules.countries import bp as countriesBP
    app.register_blueprint(countriesBP, url_prefix="/countries")
    from app.modules.profiles import bp as profilesBP
    app.register_blueprint(profilesBP, url_prefix="/profiles")
  
    @app.route("/")
    def test_page():
        return "<h1>Testing the Flask Application Factory Pattern</h1>"
    
    return app