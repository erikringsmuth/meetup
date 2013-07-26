define([
	'jquery',
	'underscore',
	'backbone',
	'text!./indexTemplate.html',
	'backboneApp/people/peopleView',
	'backboneApp/people/peopleView',
	'backboneApp/people/peopleView',
	'backboneApp/people/peopleView'
], function($, _, Backbone, indexTemplate, PeopleView, EventsView, PlacesView, ThingsView) {
	'use strict';
	
	return Backbone.View.extend({
		template: _.template(indexTemplate),
		
		events: {
			'click .navbar a': 'anchorClick'
		},
		
		render: function() {
			this.$el.html(this.template());
			this.route();
			return this;
		},
		
		route: function() {
			var view;
			switch (window.location.pathname) {
				case "/":
				case "/people":
					view = new PeopleView();
					break;
				case "/events":
					view = new EventsView();
					break;
				case "/places":
					view = new PlacesView();
					break;
				case "/things":
					view = new ThingsView();
					break;
			}
			this.$(".main-content").html(view.render().el);
		},
		
		anchorClick: function(event) {
			window.history.pushState(null, null, event.currentTarget.pathname);
			event.preventDefault();
			this.render();
		}
	});
});