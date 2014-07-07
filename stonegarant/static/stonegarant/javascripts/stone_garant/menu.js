$(function() {
  $('.menu').on('mouseenter', 'ul > li', function() {
    $(".menu .submenu").hide();
     $(this).find(".submenu").show();
  });
  $('.menu ul').on('mouseleave', '.submenu', function() {
    $(this).hide();
  });
  $('.content_holder.header').mouseenter(function() {
    $('.menu ul .submenu').hide();
  });
});