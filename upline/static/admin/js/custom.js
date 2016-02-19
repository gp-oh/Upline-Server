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

	//BINARY
	// $('.tree').tree_structure({
	// 	'add_option': false,
	// 	'edit_option': false,
	// 	'delete_option': false,
	// 	'confirm_before_delete': false,
	// 	'animate_option': false,
	// 	'fullwidth_option': false,
	// 	'align_option': 'center',
	// 	'draggable_option': false
	// });


	var enabled = $('.responsive-tree div.enabled');
	$(enabled).mouseover(function(e){
		var enabledIndex = $(enabled).index(this);
		//alert(enabledIndex);
		$('body').find('.dados').find('.enabled').find('.binary-tooltip').fadeOut();
		$('body').find('.dados').find('.enabled').eq(enabledIndex).find('.binary-tooltip').fadeIn();
		//$(this).find(".binary-tooltip").css('left',e.pageX+"px");
		//$(this).find(".binary-tooltip").css('top',(e.pageY - window.pageYOffset)+"px");
		//$(this).parents(".wrapper").find(".dados").find(".binary-tooltip").fadeIn();
		// $(this).parents("ul.tree").find("li div").css('z-index','2');
		// $(this).parents("ul.tree").find("li span").css('z-index','1');
		// $(this).css('z-index','999');
	});
	$(enabled).mouseout(function() {
		$('body').find('.dados').find('.enabled').find('.binary-tooltip').fadeOut();
	});

	$('.disabled').find('a').click(function() {
		return false;
	});

	//ADJUST MEASURES
	adjustMeasures();
	adjustBinary();


	//RESIZE
	$(window).resize(function() {
		adjustMeasures();
		adjustBinary();
	});
});


function adjustBinary(){

	var bodyWidth = $(window).width();

	if(bodyWidth <= 480){
		$('.responsive-tree').find('.enabled').each(function (index){
			var nome = $(this).find('a').text().split(" ");
			var letter01 = nome[0].charAt(0);
			var letter02 = nome[1].charAt(0);
			var finalLetters = letter01+letter02;
			$(this).find('a').text(finalLetters);
		});
	}
}

function adjustMeasures() {
	var bodyHeight = $(window).height();
	var bodyWidth = $(window).width();

	if( bodyWidth < 321 ){
		var finalHeight = bodyHeight - 100;
	}else{
		var finalHeight = bodyHeight - 160;
	}


	$('body').find('#suit-center').css({
		"height": finalHeight
	});

	if( bodyWidth < 1025 ){
		$('body').find('#suit-center').css({
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
		$('body').find('#suit-center').css({
			"width": "100%"
		});
	}
}

//Disable Double Tap Zoom iOS

(function($) {
  $.fn.nodoubletapzoom = function() {
      $(this).bind('touchstart', function preventZoom(e) {
        var t2 = e.timeStamp
          , t1 = $(this).data('lastTouch') || t2
          , dt = t2 - t1
          , fingers = e.originalEvent.touches.length;
        $(this).data('lastTouch', t2);
        if (!dt || dt > 500 || fingers > 1) return; // not double-tap

        e.preventDefault(); // double tap - prevent the zoom
        // also synthesize click events we just swallowed up
        $(this).trigger('click').trigger('click');
      });
  };
})(jQuery);
