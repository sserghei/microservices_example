from flask import Flask
from api import api_blueprint
from models import init_db, db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@db:5432/{os.getenv('POSTGRES_DB')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
init_db(app)

# Create the database tables (if they don't exist)
with app.app_context():
    db.create_all()

app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)