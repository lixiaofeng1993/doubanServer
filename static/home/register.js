$(document).ready(function () {
    //验证
    $("#phone").bind("blur", function () {
        //验证用户名长度
        if ($(this).val().length != 11) {
            //显示提示信息
            $("#accunterr").show();
            return;
        }
        //验证账号是否可用，后台验证
        $.post("/register/", {"userPhone":$(this).val()}, function (data, status) {
            if (data.data){
                //有问题
                $("#checkerr").show();
            }
        })
    });
    $("#phone").bind("focus", function () {
        $(this).val("");
        $("#accunterr").hide();
        $("#checkerr").hide();
    });
    $('#pass').bind('blur',function () {
        if ($(this).val().length < 6 || $(this).val().length > 16){
            $('#passerr').show();
        }
    });
    $("#pass").bind("focus", function () {
        $(this).val("");
        $("#passerr").hide();
        // $("#checkerr").hide();
    });
    $('#passwd').bind('blur',function () {
        if ($(this).val() != $('#pass').val()){
            $('#passwderr').show();
        }
    });
    $('#passwd').bind('focus',function () {
        $(this).val("");
        $('#passwderr').hide();

    })
});
