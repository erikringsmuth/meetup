(function() {
	'use strict';
	
	require.config({
		baseUrl: 'static/js',
		paths: {
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

	require(['jquery', 'app/indexView'], function($, indexView) {
		var view = new indexView();
		view.render();
		$('body').append(view.el);
	});
})();