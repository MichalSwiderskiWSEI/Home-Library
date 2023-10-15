from flask import Flask, blueprints
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from ..config import Config
from app import models

# Inicjalizacja rozszerzeń
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicjalizacja rozszerzeń z app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Importowanie i rejestracja blueprintów
    from .blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    
    from .blueprints.book import bp as book_bp
    app.register_blueprint(book_bp)
    
    from .blueprints.contact import bp as contact_bp
    app.register_blueprint(contact_bp)
    
    from .blueprints.init import bp as init_bp
    app.register_blueprint(init_bp)
    
    from .blueprints.rent import bp as rent_bp
    app.register_blueprint(rent_bp)
    
    from .blueprints.user import bp as user_bp
    app.register_blueprint(user_bp)

    return app


