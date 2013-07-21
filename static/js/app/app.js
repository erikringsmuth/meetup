define([
	'jquery',
	'underscore',
	'backbone',
	'text!./appTemplate.html'
], function($, _, Backbone, appTemplate) {
	'use strict';
	
	return Backbone.View.extend({
		template: _.template(appTemplate),
		
		render: function() {
			this.$el.html(this.template());
		}
	});
});