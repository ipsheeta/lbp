(function($){
$('.carousel').carousel({
	interval: 2000
});


$(document).ready(function(){
	$('.navbar-form > input').hide();
});
	$('.navbar-form > button').click(function(){
		$('.navbar-form > input').show();
	});

});