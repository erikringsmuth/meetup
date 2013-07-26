define(['backbone', './personModel'], function(Backbone, personModel) {
	'use strict';
	
	return Backbone.Collection.extend({
		url: '/api/people',
		model: personModel
	});
});