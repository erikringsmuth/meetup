define(['backbone', './personModel'], function(Backbone, personModel) {
	'use strict';
	
	return Backbone.Collection.extend({
		url: '/people',
		model: personModel
	});
});