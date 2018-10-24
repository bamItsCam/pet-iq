from flask import Flask
from api import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from api import routes

# If you add a new table, make sure to import it here!
from api.models.owner import Owner
from api.models.dog import Dog
from api.models.score import Score