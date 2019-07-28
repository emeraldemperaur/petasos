import os
import os.path
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.place import Place, PlaceList
from resources.destination import Destination, DestinationList, DestinationNameList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qoowuiemtarbia:92f206ca7e91103309393d3e77334fc79e982e7675bb8737dce7be2233c1489d@ec2-174-129-227-51.compute-1.amazonaws.com:5432/dsgqc8pcup50e'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'chrome'
api = Api(app)



#@app.before_first_request
#def create_tables():
#    db.create_all()



jwt = JWT(app, authenticate, identity)


api.add_resource(Destination, '/destination/<string:name>')
api.add_resource(Place, '/place/<string:name>')
api.add_resource(PlaceList, '/places')
api.add_resource(DestinationList, '/destinations')
api.add_resource(DestinationNameList, '/destinationnames')
api.add_resource(UserRegister,'/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
