# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

from flask import Flask
# from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
# from api.HelloApiHandler import HelloApiHandler

app = Flask(__name__)
CORS(app) #comment this on deployment
# api = Api(app)

# @app.route("/", defaults={'path':''})
# def serve(path):
#     return send_from_directory(app.static_folder,'index.html')

# api.add_resource(HelloApiHandler, '/flask/hello')

@app.route("/")
def hello_world():
    return {
      'resultStatus': 'SUCCESS',
      'message': "Hello, World!"
      }