from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)

items = []

class default(Resource):
    def get(self):
    # TODO: Add a get with container info index.html
    # return render_template('index.html')
        return jsonify({'message': 'Hello World'})
    #     return "Hello World", 200

class health(Resource):
    def get(self):
    # TODO: add the health endpoint
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