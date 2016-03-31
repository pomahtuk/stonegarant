$(document).ready(function() {
   $('.sort-switcher select').change(function () {
        try {
            yaCounter22269611.reachGoal('SORT');
        } catch (e) {
            console.log('goals available only on prod');
        }
        ga('send', {
          hitType: 'event',
          eventAction: 'ORDER'
        });
        $('#sorting_form').submit();
   });
});