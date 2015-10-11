$(document).ready(function () {
    $("#register").validate({
        rules: {
            username: "required",
            password: "required"
        }
    });
});