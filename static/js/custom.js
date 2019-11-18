$(window).scroll(function() {
    if ($(document).scrollTop() > 50) {
      $('nav').addClass('shrink');
      $('nav > .navbar-brand > img').addClass('shrink_img');
    } else {
      $('nav').removeClass('shrink');
      $('nav > .navbar-brand > img').removeClass('shrink_img');

    }
  });



  var siteCarousel = function () {
		if ( $('.nonloop-block-14').length > 0 ) {
			$('.nonloop-block-14').owlCarousel({
		    center: false,
		    items: 1,
		    loop: true,
				stagePadding: 0,
		    margin: 0,
		    autoplay: true,
		    nav: true,
		    responsive:{
	        600:{
	        	margin: 20,
	        	nav: true,
	          	items: 2
	        },
	        1000:{
	        	margin: 30,
	        	stagePadding: 0,
	        	nav: true,
	          	items: 3
	        },
	        1200:{
	        	margin: 30,
	        	stagePadding: 0,
	        	nav: true,
	          	items: 4
	        }
		    }
		});
	}

    if ( $('.nonloop-block-13').length > 0 ) {
			$('.nonloop-block-13').owlCarousel({
		    center: false,
		    items: 1,
		    loop: true,
				stagePadding: 0,
		    margin: 0,
		    autoplay: true,
		    nav: true,
		    responsive:{
	        600:{
	        	margin: 20,
	        	nav: true,
	          	items: 2
	        },
	        1000:{
	        	margin: 30,
	        	stagePadding: 0,
	        	nav: true,
	          	items: 2
	        },
	        1200:{
	        	margin: 30,
	        	stagePadding: 0,
	        	nav: true,
	          	items: 2
	        }
		    }
      });
    }
		
	};
	siteCarousel();