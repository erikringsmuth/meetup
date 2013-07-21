define([
	'jquery',
	'underscore',
	'backbone',
	'./peopleCollection',
	'text!./peopleTemplate.html'
], function($, _, Backbone, peopleCollection, peopleTemplate) {
	'use strict';
	
	return Backbone.View.extend({
		template: _.template(peopleTemplate),
		
		collection: new peopleCollection(),
		
		render: function() {
			this.collection.fetch();
			this.$el.html(this.template({model: this.collection.toJSON()}));
			return this;
		}
	});
});