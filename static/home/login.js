$(document).ready(function () {
    //验证
    $("#phone").bind("blur", function () {
        //验证账号是否可用，后台验证
        $.post("/login/", {"userPhone": $(this).val()}, function (data, status) {
            passwd = data.password;
            if (data.data) {
                //有问题
                $("#nameErr").show();
            }
        })
    });
    $("#pass").bind("blur", function () {
        //验证账号是否可用，后台验证
        $passwd = $('#pass').val();
        // console.log($passwd,passwd);
        // console.log(typeof $passwd,typeof passwd);
        if ($passwd != passwd) {

            $('#passwdErr').show()
        }
    });
    $("#phone").bind("focus", function () {
        $(this).val("");
        $("#nameErr").hide();
    });
    $("#pass").bind("focus", function () {
        $(this).val("");
        $("#passwdErr").hide();
    });
});