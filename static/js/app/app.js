define(['jquery', 'backbone'], function($, Backbone) {
	'use strict';
	
	return Backbone.View.extend({
		render: function() {
			this.$el.html("Welcome to Meetup!");
		}
	});
});