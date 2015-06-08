/**
 * Created by ilovriakov on 26/05/15.
 */
$('document').ready(function () {
    // event emitter
    var emitter = $('body');

    // image part
    var imageThumbs = $('.product-images-list .catalog-image-thumb');
    var imageHolder = $('.js-thumb-holder');
    var loadedImages = {};

    function applyOriginal(imageHolder, imageSrc) {
        imageHolder.attr('style', '');
        imageHolder.attr('src', imageSrc);
    }

    imageThumbs.click(function (evt) {
        evt.stopPropagation();
        evt.preventDefault();
        var thumb = $(this);
        var thumbSrc, imageSrc, thumbImage, preloadImage;
        var currentThumb, currentThumbWidthRatio, currentThumbHeightRatio;

        // if thumb is not active
        if (!thumb.hasClass('active')) {
            currentThumb = imageThumbs.filter('.active').find('img');
            // set active class
            imageThumbs.removeClass('active');
            thumb.addClass('active');
            // gather all data
            thumbImage = thumb.find('img');
            thumbSrc = thumbImage.attr('src');
            imageSrc = thumbImage.data('original');

            if (loadedImages[thumbSrc] === true) {
                // image already preloaded
                applyOriginal(imageHolder, imageSrc);
            } else {
                // image is not preloaded
                // set loaded flag
                loadedImages[thumbSrc] = false;
                preloadImage = new Image();

                // forcing sizing in css to scale thumb image
                currentThumbWidthRatio = imageHolder.width() / currentThumb.width();
                currentThumbHeightRatio = imageHolder.height() / currentThumb.height();
                imageHolder.height(thumbImage.height() * currentThumbHeightRatio);
                imageHolder.width(thumbImage.width() * currentThumbWidthRatio);

                imageHolder.attr('src', thumbSrc);

                preloadImage.onload = function() {
                    loadedImages[thumbSrc] = true;
                    applyOriginal(imageHolder, imageSrc);
                    preloadImage = undefined;
                };

                preloadImage.src = imageSrc;
            }
        }
    });

    // toggles part
    // global memorial price
    var memorialPriceTextHolder = $('.memorial-options-total h4');
    var currentMemorialPrice = parseInt($('.memorial-options-total').data('initila-price'), 10) || 0;

    // dimensions variables
    var stellaHeight = $('.product-details .height .value');
    var stellaWidth = $('.product-details .width .value');
    var stellaLength = $('.product-details .length .value');

    var memorialOptionsToggles = $('.memorial-options-group:not(.cvetnik)');
    var optionsContainer = $('.product-info .memorial-options');

    var initialStellaId = optionsContainer.data('stella-id');
    var currentStellaId = initialStellaId;
    var submitButton = $('.memorial-options-summary .btn_link');

    var selectedOptionsIds = {
        memorial: $('.js-memorial').data('optid'),
        stella: initialStellaId,
        // this is ugly but still
        polirovka: $('.memorial-options-group.polirovka').first().find('div').first().data('optid')
    };

    // pricing variables
    var priceOptions = {
        base: currentMemorialPrice,
        stella: 0,
        podstavka: 0,
        cvetnik: 0,
        polirovka: 1
    };

    memorialOptionsToggles.each(function () {
        var memorialOptionsToggle = $(this);
        var memorialOptions = memorialOptionsToggle.find('.memorial-options-group-option');

        memorialOptions.click(function () {
            var memorialOption = $(this);
            var priceMod = parseInt(memorialOption.data('price-mod'), 10) || 0;

            // basic scenario - just changing modificators

            // check if user trying to unselect
            if (memorialOptionsToggle.hasClass('podstavka') && memorialOption.hasClass('selected')) {
                memorialOption.removeClass('selected');
            } else {
                memorialOptions.removeClass('selected');
                memorialOption.addClass('selected');
            }

            if (memorialOptionsToggle.hasClass('polirovka')) {
                priceOptions.polirovka = 1 + (priceMod / 100);
                selectedOptionsIds.polirovka = memorialOptions.data('optid');
            } else if (memorialOptionsToggle.hasClass('podstavka')) {
                if (memorialOption.hasClass('selected')) {
                    priceOptions.podstavka = priceMod;
                    selectedOptionsIds.podstavka = memorialOptions.data('optid');
                } else {
                    priceOptions.podstavka = 0;
                    delete selectedOptionsIds.podstavka;
                }

            } else if (memorialOptionsToggle.hasClass('stella')) {
                var targetStellaId = memorialOption.data('stella-id');

                if (currentStellaId !== targetStellaId) {
                    currentStellaId = targetStellaId;
                    emitter.trigger('stella:changed', {
                        stellaId: targetStellaId,
                        stellaPrice: priceMod,
                        dimensions: memorialOption.data('dimensions')
                    });
                }
            }

            // update price text
            emitter.trigger('price:modified');

        });
    });

    submitButton.click(function () {
        console.log(selectedOptionsIds);
        submitButton.siblings('.placeholder').toggle();
    });

    // dropdown part
    var dropdownTogler = $('.memorial-options-group-option.dropdown-toggle');

    dropdownTogler.click(function() {
        var togler = $(this);

        // if we clicked at child element
        if (togler.parents('.dropdown-toggle').length > 0) {
            togler = togler.parents('.dropdown-toggle');
        }

        var dropdown = togler.next();

        if (togler.hasClass('opened')) {
            togler.removeClass('opened');
            dropdown.hide();
        } else {
            togler.addClass('opened');
            dropdown.show();
        }
    });

    dropdownTogler.each(function() {
        var ddToggle = $(this);
        var dd = ddToggle.next();
        var clearButton = dd.find('.reset-additional');
        var optionsButtons = dd.find('.additional-element-option');

        function closeDd () {
            dd.hide();
            ddToggle.removeClass('opened');
            emitter.trigger('price:modified');
        }

        clearButton.click(function() {
            ddToggle.html("Доп.<div>элементы</div>");
            ddToggle.removeClass('selected');
            optionsButtons.removeClass('selected');
            priceOptions.cvetnik = 0;
            delete selectedOptionsIds.cvetnik;
            closeDd();
        });

        optionsButtons.click(function() {
            var elem = $(this);
            optionsButtons.removeClass('selected');
            elem.addClass('selected');
            ddToggle.html(elem.html());
            ddToggle.addClass('selected');
            priceOptions.cvetnik = elem.data('price-mod');
            selectedOptionsIds.cvetnik = elem.data('optid');
            closeDd();
        });
    });

    emitter.on('price:modified', function () {
        // format price in future
        var memorialPrice = priceOptions.base + priceOptions.stella + priceOptions.podstavka + priceOptions.cvetnik;
        memorialPrice = memorialPrice * priceOptions.polirovka;
        memorialPriceTextHolder.text(memorialPrice + ' р.');
        $('.memorial-options-total-text').text('Цена в выбранной комлектации');
    });

    emitter.on('stella:changed', function (evt, data) {
        var dimensionsArr = data.dimensions.split(',');

        // basic switch
        $('.memorial-options-group:not(.stella)').hide();
        $('.memorial-options-group.stella_' + data.stellaId).show();


        var selectedPodstavka = $('.memorial-options-group.podstavka .selected');
        var selectedPolirovka = $('.memorial-options-group.polirovka .selected');
        var selectedCvetnik = $('.memorial-options-group.cvetnik .dropdown-toggle.selected');
        var cvetnikOptions = $('.memorial-options-group.cvetnik.stella_' + data.stellaId + ' .dropdown-content > div');
        var polirovkaOptions = $('.memorial-options-group.polirovka.stella_' + data.stellaId + ' .memorial-options-group-option');

        selectedOptionsIds = {
            memorial: $('.js-memorial').data('optid'),
            stella: data.stellaId
        };

        // reset all options
        priceOptions = {
            base: currentMemorialPrice,
            stella: data.stellaPrice,
            podstavka: 0,
            cvetnik: 0,
            polirovka: 1
        };


        // and keep all currently selected options
        $('.podstavka > div').removeClass('selected');
        if (selectedPodstavka.length > 0) {
             $('.podstavka.stella_' + data.stellaId + ' > div').click();
        }
        // keep polirovka variant
        if (selectedPolirovka.length > 0) {
            var pIndex = selectedPolirovka.index();
            var currentPolirovka = polirovkaOptions.get(pIndex);
            $(currentPolirovka).click();
        }

        // keep options variant
        if (selectedCvetnik.length > 0) {
            var selectedDd = selectedCvetnik.siblings('.dropdown-content');
            var ddOption = selectedDd.find('.selected');
            var cIndex = ddOption.index();
            var currentCvetnik = cvetnikOptions.get(cIndex);
            $(currentCvetnik).click();
        }


        dimensionsArr.forEach(function(item, index) {
            switch (index) {
                case 0:
                    stellaHeight.text(item + ' см.');
                    break;
                case 1:
                    stellaLength.text(item + ' см.');
                    break;
                case 2:
                    stellaWidth.text(item + ' см.');
                    break;
            }
        });

        $('.lightbox-content.complect .stella-related-info').hide();
        $('.lightbox-content.complect .stella_' + data.stellaId).show();
    });

    // lightboxes part
    var lightbox = $('.js-lightbox-container');
    var lighboxContent = $('.js-lightbox-wrapper');
    var lighboxTriggers = $('.js-lightbox-trigger');
    var lightboxClose = $('.js-lightbox-close');

    lightboxClose.click(function () {
        lightbox.hide();
        lighboxContent.attr('style', '');
        $('.js-lightbox-content').hide();
    });

    lighboxTriggers.click(function () {
        var lbHeight, wHeight, margins;

        var trigger = $(this);
        var targetLighboxClass = trigger.data('lightbox') || 'polirovka';
        var targetLightbox = $('.js-lightbox-content.' + targetLighboxClass);

        targetLightbox.show();
        lightbox.show();

        // calculations done after showing to get actual sizing
        lbHeight = lighboxContent.outerHeight();
        wHeight = $(window).height() * 0.98;

        if (lbHeight > wHeight) {
            lbHeight = wHeight;
        }

        margins = ((wHeight / 0.98) - lbHeight) / 2;

        lighboxContent.css({
            'height': lbHeight + 'px',
            'margin-top': margins
        });


    });

//$.ajaxSetup({
//     beforeSend: function(xhr, settings) {
//         function getCookie(name) {
//             var cookieValue = null;
//             if (document.cookie && document.cookie != '') {
//                 var cookies = document.cookie.split(';');
//                 for (var i = 0; i < cookies.length; i++) {
//                     var cookie = jQuery.trim(cookies[i]);
//                     // Does this cookie string begin with the name we want?
//                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                     break;
//                 }
//             }
//         }
//         return cookieValue;
//         }
//         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
//             // Only send the token to relative URLs i.e. locally.
//             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
//         }
//     }
//});
//
//$.ajax({
//	method: 'POST',
//	url: '/order-create',
//	data: {
//        memorial: 1,
//        stella: 0,
//        podstavka: 0,
//        cvetnik: 0,
//        polirovka: 1
//    }
//});


});