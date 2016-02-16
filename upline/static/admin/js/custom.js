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


	//TABLES
	$('.table').find('.checkbox').append( "<label>&nbsp</label>" );

	$('.table').find('.checkbox').find('label').click(function() {
		//alert("teste");

		var check = $(this).parent().find('input[type=checkbox]');

		if( $(check).is(':checked')) {
			$(check).prop('checked', false);
			$(this).parents('tr').removeClass('selected');
		}else{
			$(check).prop('checked', true);
			$(this).parents('tr').addClass('selected');
		}

		//$(check).prop('checked', true);

	});

	//ADJUST HEIGHT
	adjustMeasures();


	//RESIZE
	jQuery(window).resize(function() {
		adjustMeasures();
	});
});

function adjustMeasures() {
	var bodyHeight = jQuery(window).height();
	var bodyWidth = jQuery(window).width();

	if( bodyWidth < 321 ){
		var finalHeight = bodyHeight - 100;
	}else{
		var finalHeight = bodyHeight - 160;
	}


	jQuery('body').find('#suit-center').css({
		"height": finalHeight
	});

	if( bodyWidth < 1025 ){
		jQuery('body').find('#suit-center').css({
			"width": bodyWidth - 80
		});


		$('.table').wrap('<div class="wrap-table"></div>');

		$('#suit-left').find('.form-search.nav-quick-search').find('i').click(function() {
			$(this).parent().find('#quick-search').css({
				"width": '76%'
			});

			$(this).parent().find('.submit').css({
				"width": '16%',
				"z-index": '999'
			});

			$(this).css({
				"width": '16%',
				"z-index": '1'
			});

			$(this).parents('.form-search.nav-quick-search').css({
				"background": '#525155',
				"width": '250px'
			});
		});
	}

	if( bodyWidth > 1025 ){
		jQuery('body').find('#suit-center').css({
			"width": "100%"
		});
	}
}
