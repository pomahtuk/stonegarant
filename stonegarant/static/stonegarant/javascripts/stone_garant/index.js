$(function() {
    // initialize all sliders
    $('#slider .viewport').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        infinite: true,
        dots: false,
        adaptiveHeight: true,
        prevArrow: "<a class='bck' href='#'></a>",
        nextArrow: "<a class='fwd' href='#'></a>"
    });
});