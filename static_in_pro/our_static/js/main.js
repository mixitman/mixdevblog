// $(document).ready(function() {
//     // Custom
//     var stickyToggle = function(sticky, stickyWrapper, scrollElement) {
//         var stickyHeight = sticky.outerHeight();
//         var stickyTop = stickyWrapper.offset().top;
//          if (scrollElement.scrollTop() >= stickyTop){
//             stickyWrapper.height(stickyHeight);
//             sticky.addClass("is-sticky");
//         }
//         else{
//             sticky.removeClass("is-sticky");
//             stickyWrapper.height('auto');
//         }
//     };
//
//     // Find all data-toggle="sticky-onscroll" elements
//     $('[data-toggle="sticky-onscroll"]').each(function() {
//         var sticky = $(this);
//         var stickyWrapper = $('<div>').addClass('sticky-wrapper'); // insert hidden element to maintain actual top offset on page
//         sticky.before(stickyWrapper);
//         sticky.addClass('sticky');
//
//         // Scroll & resize events
//         $(window).on('scroll.sticky-onscroll resize.sticky-onscroll', function() {
//             stickyToggle(sticky, stickyWrapper, $(this));
//         });
//
//         // On page load
//         stickyToggle(sticky, stickyWrapper, $(window));
//     });
$(window).scroll(function () {
    var scroll = $(window).scrollTop();
    var lc = $('.landing-widget');
    if (scroll <= 925){
        $(lc).css('opacity', 1 - scroll / 380);
        // $(lc).css('margin-top', 7.47663551 + scroll / 48 + '%');
        // $('.landing-wrap').css('background-position-y', 40 + scroll / 2.5 + '%')
    }
});




// });


