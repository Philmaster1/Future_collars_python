from flask import Flask
from routes import register_routes
from flask_cors import CORS
from models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///warehouse.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app) # To enable CORS so that frontend can communicate with backend

    db.init_app(app)
    register_routes(app)
    return app

if __name__ == "_main_":
    app = create_app()
    with app.app_context():
        from models import Stock, Account, Transaction
        db.create_all()
        print("Database tables created.")
    app.run(debug=True)