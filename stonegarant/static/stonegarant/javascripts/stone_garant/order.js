$(document).ready(function () {
   // all magic goes here
    var $inputs = $('.input-holder input');
    var $form = $('form.order-form');

    var totalInputs = $inputs.length;

    var validations = {
        email: function (value) {
            var index = value.indexOf('@');
            // @ is not last symbol
            return index != -1 && index < value.length - 2;
        },
        phone: function (value) {
            return value.length >= 5;
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

    function runValidations ($input) {
        var $formLine = $input.parents('.form-group');
        var value = $input.val().trim();
        var validationName = $input.data('validate') || 'def';
        var validationFunction = validations[validationName];

        // also some error messages

        var valid = validationFunction(value);

        if (!valid) {
            $formLine.addClass('invalid').removeClass('valid');
        } else {
            $formLine.removeClass('invalid').addClass('valid');
        }
    }

    $inputs.change(function () {
        var $input = $(this);
        var $formLine = $input.parents('.form-group');
        var value = $input.val().trim();

        if ($formLine.hasClass('invalid') && value) {
            $formLine.removeClass('invalid').addClass('valid');
        }
    });

    $inputs.keyup(function () {
        var $input = $(this);
        var $formLine = $input.parents('.form-group');
        // on keyup validate field only if it is already invalid
        if ($formLine.hasClass('invalid')) {
            runValidations($input);
        }
    });

    $inputs.blur(function () {
        var $input = $(this);
        runValidations($input);
    });

    $form.submit(function () {
        $inputs.blur();
        var validInputs = $inputs.parents('.form-group').filter('.valid').length;
        return totalInputs === validInputs;
    });

});