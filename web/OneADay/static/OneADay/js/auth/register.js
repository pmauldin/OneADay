var registerPage = function() {
    $(document).ready(function () {
        jQuery.validator.addMethod("noSpace", function(value, element) {
            return value.indexOf(" ") < 0 && value != "";
        }, "Usernames must not contain spaces");

        $("#register").validate({
            rules: {
                username: {
                    minlength: 3,
                    noSpace: true
                },
                password: {
                    minlength: 6
                },
                passwordCheck: {
                    minlength: 6,
                    equalTo: "#password"
                }
            },
            messages: {
                passwordCheck: "Must exactly match provided password."
            }
        });
    });
};

registerPage();