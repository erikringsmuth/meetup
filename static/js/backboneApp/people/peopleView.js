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
		
		initialize: function(options) {
			this.listenTo(this.collection, "change reset add remove", this.render);
			this.collection.fetch();
		},
		
		render: function() {
			this.$el.html(this.template({model: this.collection.models}));
			return this;
		},
		
		createPerson: function(event) {
			var $createButton = $(event.currentTarget);
			this.collection.create({
				name: $createButton.siblings('[name="name"]').val(),
				username: $createButton.siblings('[name="username"]').val()
			});
		},
		
		deletePerson: function(event) {
			var $deleteButton = $(event.currentTarget);
			var person = this.collection.get($deleteButton.data('cid'));
			person.destroy();
		}
	});
});