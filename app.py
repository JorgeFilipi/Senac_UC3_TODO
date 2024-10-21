from flask import Flask
from configurations.blueprints import register_blueprints
from configurations.database import db
from configurations.config import Config
from configurations.sql_commands import create_table_tasks, create_table_users, create_root_user
from dotenv import load_dotenv
import os
from urllib.parse import quote

load_dotenv()

app = Flask(__name__)

# app.config.from_object(Config)

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')

password = quote(password)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

register_blueprints(app)

if __name__ == '__main__':
    create_table_tasks(app, db)
    create_table_users(app, db)
    create_root_user(app, db)
    app.run(debug=Config.DEBUG)