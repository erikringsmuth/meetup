import datetime
import json

import bottle


app = bottle.Bottle()

# Todo: Route to a static file that runs require.js
@app.route('/')
def index():
    return bottle.template("Welcome to meetup!")

@app.route('/status')
def status():
    return {'status': "alive"}

@app.error(404)
def error404(error):
    return "Oops! That's not supported. (404)"

# Todo: These need to be swapped out with real data from the database
@app.route('/people')
def getPeople():
    return json.dumps([{
        "@type": "http://schema.org/Person",
        "@id": "/people/erik.ringsmuth",
        "name": "Erik Ringsmuth"
    }])

@app.route('/people/<username>', method='GET')
def getPerson(username):
    return json.dumps({
        "@type": "http://schema.org/Person",
        "@id": "/people/" + username,
        "name": "Erik Ringsmuth"
    })

@app.route('/events')
def getPeople():
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
def getPerson(id):
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


app.run(host='localhost', port=8080, debug=True)
