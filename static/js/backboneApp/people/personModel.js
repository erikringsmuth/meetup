define(['backbone'], function(Backbone) {
	'use strict';
	
	return Backbone.Model.extend({
		url: function() {
			var url = '/api/people';
			if (this.id) {
				url = url + '/' + this.id;
			}
			return url;
		}
	});
});