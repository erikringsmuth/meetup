(function() {
	'use strict';
	
	require.config({
		baseUrl: 'static/js',
		paths: {
			'text': 'lib/require/text',
			'jquery': 'lib/jquery/jquery',
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

	require(['jquery', 'backboneApp/index/indexView'], function($, indexView) {
		var view = new indexView();
		$('body').html(view.el);
		view.render();
	});
})();