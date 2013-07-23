define([
	'jquery',
	'underscore',
	'backbone',
	'./peopleCollection',
	'./personModel',
	'text!./peopleTemplate.html'
], function($, _, Backbone, PeopleCollection, PersonModel, peopleTemplate) {
	'use strict';
	
	return Backbone.View.extend({
		template: _.template(peopleTemplate),
		
		collection: new PeopleCollection(),
		
		events: {
			'click button[name="create"]': 'createPerson',
			'click button[name="delete"]': 'deletePerson'
		},
		
		render: function() {
			var that = this;
			this.collection.fetch({success: function(collection, response, options) {
				that.$el.html(that.template({model: collection.models}));
			}});
			return this;
		},
		
		createPerson: function(event) {
			var $createButton = $(event.currentTarget);
			new PersonModel({
				name: $createButton.siblings('[name="name"]').val(),
				username: $createButton.siblings('[name="username"]').val()
			}).save();
			this.render();
		},
		
		deletePerson: function(event) {
			var $deleteButton = $(event.currentTarget);
			var person = this.collection.get($deleteButton.data('cid'));
			person.destroy();
			this.render();
		}
	});
});