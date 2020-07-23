from datetime import datetime
from flask import Flask, jsonify
from flask_restful import Resource, Api
import os
import pytz

app = Flask(__name__)
api = Api(app)

class default(Resource,):
    def get(self):
        localTime = pytz.timezone("GMT")
        time = datetime.now().replace(microsecond=0).replace(tzinfo=pytz.utc)
        time = time.astimezone(localTime)


        if "HOSTNAME" in os.environ:
            hostname = os.environ['HOSTNAME']
            jsonResponse = {
                'aws_hostname': hostname,
                'greeting': 'Hello World',
                'now': time
            }
        else:
            jsonResponse = {
                'greeting': 'Hello World',
                'now': time
            }
        return jsonify(jsonResponse)

class health(Resource):
    def get(self):

        return "Healthy", 200

# Env Variables
if "APP_PORT" in os.environ:
    port = os.environ['APP_PORT']
else:
    port = 5000

if "APP_HOST" in os.environ:
    host = os.environ['APP_HOST']
else:
    host = '127.0.0.1'

if "APP_DEBUG" in os.environ:
    debug = os.environ['APP_DEBUG']
else:
    debug = True

api.add_resource(default, '/v1/api')
api.add_resource(health, '/healthz')

app.run(host=host, port=port, debug=debug)