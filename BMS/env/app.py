from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from resources.errors import errors

app = Flask(__name__)
# app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app, errors=errors)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/User'
}

#for pytest
# app.config['MONGODB_SETTINGS'] = {
#     'host': 'mongodb://localhost/User-test'
# }
app.config['PROPAGATE_EXCEPTIONS'] = False

initialize_db(app)
initialize_routes(api)

app.run(debug=True)
