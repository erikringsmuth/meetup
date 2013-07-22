define([
	'jquery',
	'underscore',
	'backbone',
	'./peopleCollection',
	'text!./peopleTemplate.html'
], function($, _, Backbone, PeopleCollection, peopleTemplate) {
	'use strict';
	
	return Backbone.View.extend({
		template: _.template(peopleTemplate),
		
		collection: new PeopleCollection(),
		
		render: function() {
			var that = this;
			this.collection.fetch({success: function(collection, response, options) {
				that.$el.html(that.template({model: response}));
			}});
			return this;
		}
	});
});