import datetime
import json
import sqlite3

import bottle

# Database set up
connection = sqlite3.connect('meetup.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS people (username TEXT, name TEXT)')
cursor.close()

app = bottle.Bottle()

# The base route loads a simple html file that starts require.js
@app.route('/')
def index():
    return bottle.static_file('index.html', root='static')

# Route all files in the /static directory
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='static')

@app.route('/api/status')
def status():
    return {'status': 'alive'}

@app.error(404)
def error404(error):
    return "Oops! That's not supported. (404)"

@app.route('/api/people', method='POST')
def create_person():
    person = bottle.request.json
    username = person['username']
    name = person['name']
    cursor = connection.cursor()
    cursor.execute('INSERT INTO people VALUES(?,?)', (username, name))
    cursor.close()
    person['@type'] = 'http://schema.org/Person'
    person['@id'] = '/api/person/' + username
    return json.dumps(person)

@app.route('/api/people')
def get_people():
    cursor = connection.cursor()
    people = []
    for row in cursor.execute('SELECT * FROM people'):
        person = {}
        person['id'] = row[0]
        person['username'] = row[0]
        person['name'] = row[1]
        person['@type'] = 'http://schema.org/Person'
        person['@id'] = '/api/person/' + person['username']
        people.append(person)
    cursor.close()
    return json.dumps(people)

@app.route('/api/people/<username>', method='DELETE')
def delete_person(username):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM people WHERE username='" + username + "'")
    cursor.close()
    return

# Todo: These need to be swapped out with real data from the database
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
