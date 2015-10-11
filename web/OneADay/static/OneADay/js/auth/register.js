$(document).ready(function () {
    $("#register").validate({
        rules: {
            username: "required",
            email: "required",
            password: {
                required: true,
                minlength: 6
            },
            passwordCheck: {
                required: true,
                minlength: 6,
                equalTo: "#password"
            }
        },
        messages: {
            passwordCheck: "Must exactly match provided password."
        }
    });
});