from db import db

class DestinationModel(db.Model):
    __tablename__ = 'destinations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    bannerimg_url = db.Column(db.String(140))
    time_url = db.Column(db.String(140))
    weather_url = db.Column(db.String(140))
    currency = db.Column(db.String(4))
    itu_countrycode = db.Column(db.String(4))



    places = db.relationship('PlaceModel', lazy='dynamic')


    def __init__(self, name, bannerimg_url, time_url, weather_url, currency, itu_countrycode):
        self.name = name
        self.bannerimg_url = bannerimg_url
        self.time_url = time_url
        self.weather_url = weather_url
        self.currency = currency
        self.itu_countrycode = itu_countrycode


    def json(self):
        return {'name': self.name,'bannerimg_url': self.bannerimg_url ,'time_url': self.time_url,
        'weather_url': self.weather_url,'currency': self.currency,'itu_countrycode': self.itu_countrycode,'places': [place.json() for place in self.places.all()]}

    def namelistjson(self):
        return {'name': self.name}



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
