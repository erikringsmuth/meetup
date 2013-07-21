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

	require(['jquery', 'app/index/indexView'], function($, indexView) {
		var view = new indexView();
		$('body').html(view.el);
		view.render();
	});
})();