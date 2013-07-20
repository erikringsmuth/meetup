import bottle
import json

app = bottle.Bottle()

@app.route('/', method='GET')
@app.route('/status', method='GET')
def index():
    return {'status': "alive"}

@app.error(404)
def error404(error):
    return "Oops! That's not suported"

@app.route('/users', method='GET')
def getUsers():
    return json.dumps([{'name': "Erik Ringsmuth"}, {'name': "Jon Doe"}])

@app.route('/wildcard', method='GET')
@app.route('/wildcard/<wildcard>', method='GET')
def getWildcard(wildcard='*'):
    return bottle.template("You entered {{wildcard}}!", wildcard=wildcard)

app.run(host='localhost', port=8080, debug=True, reloader=True)
