from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.place import Place, PlaceList
from resources.destination import Destination, DestinationList, DestinationNameList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yniicmaipxgjns:bc4aa173b80e7d809907de6d63e7b259f989fb041d4e9f11ce42af4c9e66a69e@ec2-54-243-208-234.compute-1.amazonaws.com:5432/d32ai5ror9u530'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'chrome'
api = Api(app)







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
