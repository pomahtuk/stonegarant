$(function() {
    var $container = $('.catalog-list--container'),
        $memorialsList = $container.find('ul.cf'),
        $buttonHolder = $container.find('.load-more-wrapper');


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

    // ajax updater
    $container.on('click', '.js-load-more', function () {
        var $elem = $(this),
            elemData = $elem.data();

        var request = $.ajax({
            method: 'POST',
            url: '/ajax_catalog.html',
            data: $.extend({}, elemData, {
                page: elemData.page + 1
            }),
            headers: {
                'X-CSRFToken': elemData.csrfmiddlewaretoken
            }
        });

        request.done(function(data) {
            var $data = $(data),
                $memorials = $data.find('.single-memorial'),
                $button = $data.find('.js-load-more');

            $memorialsList.append($memorials);
            $buttonHolder.html($button);
        });

        request.fail(function() {
            console.log(error);
        });

        // initialize preloader instead of button

        // make a request to server

        // once done - remove preloader, append contents to list,
        // and button element to holder

        return false;
    });
});