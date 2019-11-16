$(document).ready(function(){
  $(".owl-carousel").owlCarousel({
    loop:true,
    nav:true,
    touchDrag:true,
    mouseDrag:true,
    autoplay:true,
    autoWidth:true,
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
        },
        1024:{
            items:4,
        }
    }
  }

  );
});

$(window).scroll(function() {
    if ($(document).scrollTop() > 50) {
      $('nav').addClass('shrink');
    } else {
      $('nav').removeClass('shrink');
    }
  });
  