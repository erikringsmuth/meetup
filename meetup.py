import datetime
import json

import bottle


app = bottle.Bottle()

# The base route loads a simple html file that starts require.js
@app.route('/')
def index():
    return bottle.static_file('index.html', root='static')

# Route all files in the /static directory
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='static')

# Use to smoke check the server after a deploy
@app.route('/status')
def status():
    return {'status': "alive"}

@app.error(404)
def error404(error):
    return "Oops! That's not supported. (404)"

# Todo: These need to be swapped out with real data from the database
@app.route('/people')
def get_people():
    return json.dumps([{
        "@type": "http://schema.org/Person",
        "@id": "/people/erik.ringsmuth",
        "name": "Erik Ringsmuth"
    }])

@app.route('/people/<username>', method='GET')
def get_person(username):
    return json.dumps({
        "@type": "http://schema.org/Person",
        "@id": "/people/" + username,
        "name": "Erik Ringsmuth"
    })

@app.route('/events')
def get_events():
    return json.dumps([{
        "@type": "http://schema.org/Event",
        "@id": "/events/1",
        "id": "guid",
        "attendees": [],
        "name": "string",
        "description": "string",
        "location": {},
        "startDate": datetime.datetime.now().isoformat(),
        "endDate": datetime.datetime.now().isoformat(),
        "duration": ""
    }])

@app.route('/events/<id>', method='GET')
def get_event(id):
    return json.dumps({
        "@type": "http://schema.org/Event",
        "@id": "/events/" + id,
        "id": "guid",
        "attendees": [],
        "name": "string",
        "description": "string",
        "location": {},
        "startDate": datetime.datetime.now().isoformat(),
        "endDate": datetime.datetime.now().isoformat(),
        "duration": ""
    })

@app.route('/places')
def get_places():
    return json.dumps([{
        "@type": "http://schema.org/Place",
        "@id": "/places/1",
        "id": "guid",
        "name": "string",
        "description": "string",
        "address": {
            "addressCountry": "string",
            "addressLocality": "string",
            "addressRegion": "string",
            "postalCode": "string",
            "postOfficeBoxNumber": "string",
            "streetAddress": "string"
        }
    }])

@app.route('/places/<id>', method='GET')
def get_place(id):
    return json.dumps({
        "@type": "http://schema.org/Place",
        "@id": "/places/" + id,
        "id": "guid",
        "name": "string",
        "description": "string",
        "address": {
            "addressCountry": "string",
            "addressLocality": "string",
            "addressRegion": "string",
            "postalCode": "string",
            "postOfficeBoxNumber": "string",
            "streetAddress": "string"
        }
    })

@app.route('/things')
def get_things():
    return json.dumps([{
        "@type": "http://schema.org/Thing",
        "@id": "/things/1",
        "id": "guid",
        "name": "string",
        "description": "string"
    }])

@app.route('/things/<id>', method='GET')
def get_thing(id):
    return json.dumps({
        "@type": "http://schema.org/Thing",
        "@id": "/things/" + id,
        "id": "guid",
        "name": "string",
        "description": "string"
    })

app.run(host='localhost', port=8080, debug=True)
