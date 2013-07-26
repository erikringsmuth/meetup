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
@app.route('/api/status')
def status():
    return {'status': "alive"}

@app.error(404)
def error404(error):
    return "Oops! That's not supported. (404)"

# Todo: These need to be swapped out with real data from the database
@app.route('/api/people')
def get_people():
    return json.dumps([{
        "@type": "http://schema.org/Person",
        "@id": "/people/erik.ringsmuth",
        "id": "erik.ringsmuth",
        "name": "Erik Ringsmuth"
    }])

@app.route('/api/people/<username>', method='GET')
def get_person(username):
    return json.dumps({
        "@type": "http://schema.org/Person",
        "@id": "/people/" + username,
        "id": username,
        "name": "Erik Ringsmuth"
    })

@app.route('/api/events')
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

@app.route('/api/events/<id>', method='GET')
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

@app.route('/api/places')
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

@app.route('/api/places/<id>', method='GET')
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

@app.route('/api/things')
def get_things():
    return json.dumps([{
        "@type": "http://schema.org/Thing",
        "@id": "/things/1",
        "id": "guid",
        "name": "string",
        "description": "string"
    }])

@app.route('/api/things/<id>', method='GET')
def get_thing(id):
    return json.dumps({
        "@type": "http://schema.org/Thing",
        "@id": "/things/" + id,
        "id": "guid",
        "name": "string",
        "description": "string"
    })

# Catch all other routes and have them load the main JS app
@app.route('/<:path>')
def index():
    return bottle.static_file('index.html', root='static')

app.run(host='localhost', port=8080, debug=True)
