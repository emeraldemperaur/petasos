from flask_restful import Resource, reqparse, Api
from models.destination import DestinationModel


class Destination(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('bannerimg_url',
        required=True,
        help="Every Petasos Place Location needs a bannerimg_url argument!"

    )
    parser.add_argument('time_url',
        required=True,
        help="Every Petasos Place Location needs an abouttext description argument!"

    )
    parser.add_argument('weather_url',
        required=True,
        help="Every Petasos Place Location needs a website_url argument!"

    )
    parser.add_argument('currency',
        required=True,
        help="Every Petasos Place Location needs a phone_number argument!"

    )
    parser.add_argument('itu_countrycode',
        required=True,
        help="Every Petasos Place Location needs an email_address argument!"

    )
    parser.add_argument('itu_countrycode',

        help="Every Petasos Place Location needs an email_address argument!"

    )


    def get(self, name):
        destination = DestinationModel.find_by_name(name)
        if destination:
            return destination.json()
        return {'message': "Petasos Destination '{}' was not found on the Hermes-Venus database".format(name)}, 404

    def post(self, name):
        if DestinationModel.find_by_name(name):
            return {'message': "Petasos Destination with the name '{}' already exists on the Hermes-Venus database".format(name)}, 400

        data = Destination.parser.parse_args()
        destination = DestinationModel(name, data['bannerimg_url'], data['time_url'], data['weather_url'], data['currency'], data['itu_countrycode'])
        try:
            destination.save_to_db()
        except:
            return {'message': "Error occured while creating the '{}' Petasos Destination entity on the Hermes-Venus database!".format(name)}, 500

        return destination.json(), 201

    def delete(self, name):
        destination = DestinationModel.find_by_name(name)
        if destination:
            destination.delete_from_db()

        return {'message': "The Petasos Destination '{}' was successfully deleted from the Hermes-Venus database!".format(name)}




class DestinationList(Resource):
    def get(self):
        return {'destinations': [destination.json() for destination in DestinationModel.find_all()]}


class DestinationNameList(Resource):
    def get(self):
        return {'destinationnames': [destination.namelistjson() for destination in DestinationModel.find_all()]}
