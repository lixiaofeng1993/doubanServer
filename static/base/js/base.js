$(document).ready(function(){
    document.documentElement.style.fontSize = innerWidth / 10 + "px";

    //拿出地址栏里的地址
    var urlstr = location.href;
    //  http://127.0.0.1:8000/market/
    arr = urlstr.split("/");
    $span = $(document.getElementById(arr[3]));
    imgurl = "url(/static/axf/base/img/"+arr[3]+"1.png) no-repeat";
    $span.css("background", imgurl);
    $span.css("background-size", "0.54rem")

});