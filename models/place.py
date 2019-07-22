from db import db

class PlaceModel(db.Model):
    __tablename__ = 'places'

    name = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)
    bannerimg_url = db.Column(db.String(140))
    abouttext = db.Column(db.String(200))
    website_url = db.Column(db.String(90))
    phone_number = db.Column(db.String(15))
    email_address = db.Column(db.String(30))
    placetype = db.Column(db.String(13))

    destination_name = db.Column(db.String, db.ForeignKey('destinations.name'), nullable=False)
    destination = db.relationship('DestinationModel')

    def __init__(self, name, bannerimg_url, abouttext, website_url, phone_number, email_address, placetype, destination_name):
        self.name = name
        self.bannerimg_url = bannerimg_url
        self.abouttext = abouttext
        self.website_url = website_url
        self.phone_number = phone_number
        self.email_address = email_address
        self.placetype = placetype
        self.destination_name = destination_name

    def json(self):
        return {'name': self.name, 'bannerimg_url': self.bannerimg_url, 'abouttext': self.abouttext, 'website_url': self.website_url,
        'phone_number': self.phone_number, 'email_address': self.email_address, 'placetype': self.placetype,
        'destination_name': self.destination_name}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
