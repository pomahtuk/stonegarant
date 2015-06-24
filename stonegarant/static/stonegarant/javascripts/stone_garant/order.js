$(document).ready(function () {
   // all magic goes here
    var $inputs = $('.input-holder input');
    var $form = $('form.order-form');

    var validInputs = 0;
    var totalInputs = $inputs.length;

    $inputs.change(function () {
        var $input = $(this);
        var value = $input.val().trim();

        if ($input.hasClass('invalid') && value) {
            validInputs += 1;
            $input.removeClass('invalid').addClass('valid');
        }
    });

    $inputs.blur(function () {
        var $input = $(this);
        var value = $input.val().trim();

        if (!value) {
            validInputs > 0 ? validInputs -= 1 : validInputs = 0;
            $input.addClass('invalid').removeClass('valid');
        } else {
            validInputs += 1;
            $input.removeClass('invalid').addClass('valid');
        }
    });

    $form.submit(function () {
        return totalInputs === validInputs;
    });

});