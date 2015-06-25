$(document).ready(function () {
   // all magic goes here
    var $inputs = $('.input-holder input');
    var $form = $('form.order-form');

    var validInputs = 0;
    var totalInputs = $inputs.length;

    var validations = {
        email: function (value) {
            return value.indexOf('@') != -1;
        },
        phone: function (value) {
            return value.length > 5;
        },
        name: function (value) {
            return value.length > 3;
        },
        city: function (value) {
            return value.length > 3;
        },
        def: function (value) {
            return value.length > 0;
        }
    };

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
        var validationName = $input.data('validation') || 'def';
        var validationFunction = validations[validationName];

        // also some error messages

        var valid = validationFunction(value);

        if (!valid) {
            validInputs > 0 ? validInputs = validInputs - 1 : validInputs = 0;
            $formLine.addClass('invalid').removeClass('valid');
        } else {
            validInputs += 1;
            $formLine.removeClass('invalid').addClass('valid');
        }
    });

    $form.submit(function () {
        //console.log(totalInputs, validInputs);
        $inputs.blur();
        return totalInputs === validInputs;
    });

});