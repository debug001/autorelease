$(document).ready(function(){
    $("select").attr("multiple", "multiple");
    $("#groupid").change(function(){
        $("#current_user option").remove();
        var group = $("#groupid").val();
        $.post("/ajax/get_current_user/", {group:group}, function(data){
            var strs= new Array();
            strs = data.split("|");
            for (var i =0; i<strs.length; i++) {
                if (strs[i]) {
                    $("#current_user").append("<option value='" + strs[i]+ "'>" +strs[i]+"</option>");
                };
            };
        });
    });

    $("#add").click(function(){
        var user = $("#user_list").val();
        var groupid = $("#groupid").val();
        $.post("/ajax/current_user_add/", {user:user, groupid:groupid}, function(data){
            var strs= new Array();
            strs = data.split("|");
            for (var i =0; i<strs.length; i++) {
                if (strs[i]) {
                    $("#current_user").append("<option value='" + strs[i]+ "'>" +strs[i]+"</option>");
                };
            };

        });


    });



});
