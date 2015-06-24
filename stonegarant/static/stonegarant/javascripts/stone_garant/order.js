$(document).ready(function () {
   // all magic goes here
    var $inputs = $('.input-holder input');
    var $form = $('form.order-form');

    var validInputs = 0;
    var totalInputs = $inputs.length;

    $inputs.change(function () {
        var $input = $(this);
        var $formLine = $input.parents('.form-group');
        var value = $input.val().trim();

        if ($input.hasClass('invalid') && value) {
            validInputs += 1;
            $formLine.removeClass('invalid').addClass('valid');
        }
    });

    $inputs.blur(function () {
        var $input = $(this);
        var $formLine = $input.parents('.form-group');
        var value = $input.val().trim();

        if (!value) {
            validInputs > 0 ? validInputs = validInputs - 1 : validInputs = 0;
            $formLine.addClass('invalid').removeClass('valid');
        } else {
            validInputs += 1;
            $formLine.removeClass('invalid').addClass('valid');
        }
    });

    $form.submit(function () {
        console.log(totalInputs, validInputs);
        return totalInputs === validInputs;
    });

});