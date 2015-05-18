$(document).ready(function() {
   $('.sort-switcher').change(function () {
       var $select = $(this);
       console.log($select.val());
   });
});