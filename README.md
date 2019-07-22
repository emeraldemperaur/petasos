# Petasos API
Petasos /peh· tuh· zowz/ is a bespoke, scalable Flask-RESTful microservice built to receive destination or place data requests from an authenticated client <mobile + web + hybrid + OS + Embedded> application and return appropriate response results pertinent to the client HTTP request method - DB data privately curated from destination cities & places of interest across the globe. 

API URL >_ https://petasosapi.herokuapp.com

API Documentation >_ https://www.emekaegwim.com/petasos/index.html

## API Endpoints

**GET, POST, PUT, DELETE HTTP request method(s)**

/destination/string:name GET, POST, PUT, DELETE

/place/string:name GET, POST, PUT, DELETE

/destinations GET only

/places GET only

/destinationnames GET only

### JWT AUTHENTICATION ENABLED
JSON Web Tokens implemented to facilitate secure API User Authentication and Log In
