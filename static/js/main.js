(function() {
	'use strict';
	
	require.config({
		baseUrl: 'static/js',
		paths: {
			'text': 'lib/require/text',
			'jquery': 'lib/jquery/jquery-2.0.3',
			'underscore': 'lib/underscore/underscore',
			'backbone': 'lib/backbone/backbone'
		},
		shim: {
			'jquery': {
				exports: '$'
			},
			'underscore': {
				exports: '_'
			},
			'backbone': {
				deps: ['underscore', 'jquery'],
				exports: 'Backbone'
			}
		}
	});

	require(['jquery', 'app/app'], function($, app) {
		var view = new app();
		$('body').html(view.el);
		view.render();
	});
})();