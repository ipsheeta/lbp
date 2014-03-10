(function($) {
$('.postdate').each(function(){
	$('#sidecolumn > ul').append('<li><a href="#">' + $(this).data('month')+ '</a></li>');
});
var counter = 1;
$('.postdate').each(function(){
	$('#subnav').append('<li id="scroll-' + counter + '"><a href="#">' + $(this).data('month')+ '</a></li>');
	counter++;
});
	var position = new Array();
	$('.postdate').each(function(){
			position.push($(this));
		});
	var currentActive = $('#scroll-1');

	$(document).scroll(function(e){
		for (var i = 0; i < position.length; i++) {
			var diff = position[i].offset().top - $(document).scrollTop();

			if (diff < 0 && diff > -5 ) {
				$('#scroll-'+(i+1)).addClass('active');
				if (currentActive !== position[i]) {
					currentActive.removeClass('active');
					currentActive = $('#scroll-'+(i+1));
				}
			}
		}
	});
	// return $(document).scroll(function(e) {
	// 	var target = $('.postdate').first().offset();
	// 	var diff = target.top - $(document).scrollTop();
	// 	if (diff == 0) {
	// 		alert('bling!');
	// 	}
	
	// });
})(jQuery);
	// $(document).ready(function(){
	// 	$(document).scroll(function(e) {
	// 		min: $('.subnav_fixed').offset().top,
	// 		onEnter: function(element, position){
	// 			$('.subnav_fixed').addCLass('fixed');
	// 			$(id + '-scrolling').offset();
	// 		},
	// 		onLeave: function(element, position){
	// 			$('.subnav_fixed').removeClass('fixed');
	// 		}
	// 	});
	// });

$('.carousel').carousel({
	interval: 2000
})

$(document).ready(function(){
	$('.navbar-form, input').hide();
});
	$('.navbar-form, button').click(function(){
		$('.navbar-form, input').show();
	});


