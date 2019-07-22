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
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xxjgsgqtzkrkpf:75d1805913d9ee40119a14f88f64c13392768287a59f2570a0ec9e9a50fc55df@ec2-174-129-209-212.compute-1.amazonaws.com:5432/dbr1qer8bl4vea'
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
