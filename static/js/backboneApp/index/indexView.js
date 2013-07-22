define([
	'jquery',
	'underscore',
	'backbone',
	'text!./indexTemplate.html',
	'backboneApp/people/peopleView'
], function($, _, Backbone, indexTemplate, PeopleView) {
	'use strict';
	
	return Backbone.View.extend({
		template: _.template(indexTemplate),
		
		render: function() {
			this.$el.html(this.template());
			this.$el.append(new PeopleView().render().el);
			return this;
		}
	});
});