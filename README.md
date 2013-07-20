## Meetup
Ping your friends and meet up!

This project is mostly an academic exercise. I figure it's time to learn Python and Angular.js so here we go!

## Main features I want
- Ping friends to see who wants to meet up
- Check-in: who, what, where, when
- Push events would be awesome
- Create groups
- Use of JSON-LD to link to anything external (or internal)
- Store login credentials in cookie (auth token)

## Tech
- sqlite
- Python
- Bottle.py for REST API
- node.js
- grunt.js
- require.js
- angular.js (possibly write the UI in multiple libraries including backbone.js and ember.js)
- Twitter Bootstrap
- JSON-LD and schema.org

## Examples
- Ping -> who: lunch group, what: lunch
- Ping -> who: lunch group, what: lunch, where: cafe d, when: 11:45am

## JSON modeled after Schema.org
```
// The main concepts are who (Person), what (Event), where (Place), when (Date ISO8601)
// I also want to be able to do basic tags (Thing)

GET /people
GET /people/<username>
{
	"@type": "http://schema.org/Person",
	"@id": "/people/" + username,
	"name": "Erik Ringsmuth"
}

GET /events
GET /events/<id>
{
	"@type": "http://schema.org/Event",
	"@id": "/events/" + id,
	id: "guid",
	attendees: [],
	name: "string",
	description: "string",
	location: {}, // Place
	startDate: new Date(),
	endDate: new Date(),
	duration: "" // Duration
}

GET /places
GET /places/<id>
{
	"@type": "http://schema.org/Place",
	"@id": "/places/" + id,
	id: "guid",
	name: "string",
	description: "string",
	address: {
		addressCountry: "string",
		addressLocality: "string",
		addressRegion: "string",
		postalCode: "string",
		postOfficeBoxNumber: "string",
		streetAddress: "string"
	}
}

GET /things
GET /things/<id>
{
	"@type": "http://schema.org/Thing",
	"@id": "/things/" + id,
	id: "guid",
	name: "string",
	description: "string"
}
```