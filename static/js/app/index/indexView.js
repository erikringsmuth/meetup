define([
	'jquery',
	'underscore',
	'backbone',
	'text!./indexTemplate.html',
	'app/people/peopleView'
], function($, _, Backbone, indexTemplate, peopleView) {
	'use strict';
	
	return Backbone.View.extend({
		template: _.template(indexTemplate),
		
		render: function() {
			this.$el.html(this.template());
			var people = new peopleView();
			this.$el.append(people.render().el);
			return this;
		}
	});
});