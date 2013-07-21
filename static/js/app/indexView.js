require(['jquery', 'backbone'], function($, Backbone) {
	'use strict';
	
	return Backbone.View.extend({
		render: function() {
			this.$el.html("<div>W00T! Backbone is working!</div>");
		}
	});
});