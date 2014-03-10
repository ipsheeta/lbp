var timeOut = 45;
$('document').ready(function(){
	$('.greenBox').hide(function(){
	});
});
$('.close-btn').click(function(){
    $('.greenBox').hide();
    console.log($(this).parent().parent());
    parentElem = $(this).parent().parent().parent();
    $(parentElem).find('.greenBox').show();
});
$('#cta').click(function(){
    $('#rightCol').trigger('click');
});
$('.btn').click(function(e){
	var link = ($(this).attr('href'));
	$('.greenBox').hide();
	//$(link + '-signup').show();
	scrollToUs(link, this);
	e.preventDefault();
});
function scrollToUs(to, from){
	var currentPosition = $(document).scrollTop();
	var targetPosition = $(to).offset();
	var diff = targetPosition.top - currentPosition;
	var distance = diff;
	var target = targetPosition.top;
	
	function scrolling(){
		if(distance == 0) {
			return
		} else {
			distance = distance - 100;
			if(distance < 0){
				distance = 0;
			}
			$(document).scrollTop(target - distance);
			setTimeout(scrolling, timeOut);
		};
	};

	scrolling();
};
