from flask_restful import Api, Resource, reqparse
from flask_jwt import jwt_required
from models.place import PlaceModel



class Place(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('bannerimg_url',
        required=True,
        help="Every Petasos Place Location needs a bannerimg_url argument!"

    )
    parser.add_argument('abouttext',
        required=True,
        help="Every Petasos Place Location needs an abouttext description argument!"

    )
    parser.add_argument('website_url',
        required=True,
        help="Every Petasos Place Location needs a website_url argument!"

    )
    parser.add_argument('phone_number',
        required=True,
        help="Every Petasos Place Location needs a phone_number argument!"

    )
    parser.add_argument('email_address',
        required=True,
        help="Every Petasos Place Location needs an email_address argument!"

    )
    parser.add_argument('placetype',
        required=True,
        help="The placetype field cannot be left null (Try abode, food, entertainment,food, edification, popular or poi)!"

    )
    parser.add_argument('destination_id',
        type=float,
        required=True,
        help="Every Petasos Place Location needs a related destination_id!"

    )
    parser.add_argument('destination_name',
        required=True,
        help="Every Petasos Place Location needs a related destination_name!"

    )

    @jwt_required()
    def get(self, name):
        place = PlaceModel.find_by_name(name)
        if place:
            return place.json()
        return {'message': "The Petasos Location '{}' was not found on the Hermes-Venus database".format(name)}, 404



    def post(self, name):
        if PlaceModel.find_by_name(name):
            return {'message': "A Petasos Location with the name '{}' already exists on the Hermes-Venus database.".format(name)}, 400

        data = Place.parser.parse_args()
        place = PlaceModel(name, data['bannerimg_url'], data['abouttext'], data['website_url'], data['phone_number'], data['email_address'], data['placetype'], data['destination_id'], data['destination_name'])

        try:
            place.save_to_db()
        except:
            return {"message": "An Error occured uploading the Petasos Location with the name '{name}' and '{destination_id}' into the Hermes-Venus database".format(name, data['destination_id'])}, 500

        return place.json(), 201


    def delete(self, name):
        place = PlaceModel.find_by_name(name)
        if place:
            place.delete_from_db()

        return {'message': "The Petasos Location '{}' was successfully deleted from the Hermes-Venus".format(name)}



    def put(self, name):
        data = Place.parser.parse_args()
        place = PlaceModel.find_by_name(name)


        if place is None:
            place = PlaceModel(name, data['bannerimg_url'], data['abouttext'], data['website_url'], data['phone_number'], data['email_address'], data['placetype'], data['destination_id'], data['destination_name'])
        else:
            place.bannerimg_url = data['bannerimg_url']
            place.abouttext = data['abouttext']
            place.website_url = data['website_url']
            place.phone_number = data['phone_number']
            place.email_address = data['email_address']
            place.placetype = data['placetype']
            place.destination_id = data['destination_id']
            place.destination_name = data['destination_name']

        place.save_to_db()

        return place.json()



class PlaceList(Resource):
    def get(self):
        return {'places': [place.json() for place in PlaceModel.find_all()]}
