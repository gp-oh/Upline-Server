// Written for jQuery
$(function(){
	//MENU HEADER
	$('#user-menu').find('dt').click(function() {
		$(this).toggleClass('active');
		$(this).parents('dl').find('dd').slideToggle("fast");
	});




	//SIDEBAR MENU
	$('#left-nav').find('li:first').addClass("inicio");

	$('#left-nav').find('li:not(.inicio)').find('a.no-link').click(function() {
		$(this).parent().siblings('li').find('ul').slideUp('fast');
		$(this).parent().find('ul').slideToggle('fast');
		return false;
	});




	//ADJUST HEIGHT
	adjustHeight();


	//RESIZE
	jQuery(window).resize(function() {
		adjustHeight();
	});
});

function adjustHeight() {
	var bodyHeight = jQuery(window).height();
	var finalHeight = bodyHeight - 160;

	jQuery('body').find('#suit-center').css({
		"height": finalHeight
	});
}
