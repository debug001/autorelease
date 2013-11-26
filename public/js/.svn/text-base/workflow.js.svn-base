$(document).ready(function(){
    $("select").attr("multiple", "multiple");

    $("#group_list").change(function(){
        $("#group_user_list option").remove();
        var group =  $("#group_list").val();
        $.post("/ajax/get_user/", {group:group}, function(data){
            var strs= new Array();
            strs = data.split("|");
            for (var i =0; i<strs.length; i++) {
                if (strs[i]) {
                    $("#group_user_list").append("<option value='" + strs[i]+ "'>" +strs[i]+"</option>");
                };
            };
        });
    });

    $("#add_group").click(function(){
        var group_list = $("#group_list").val();
        var project = $("#current_group").attr("project");
        var status = $("#current_group").attr("status");
        $.post("/ajax/unique_group_add/", {group_list:group_list, status:status, project:project}, function(data){
            var strs= new Array();
            strs = data.split("|");
            for (var i =0; i<strs.length; i++) {
                if (strs[i]) {
                    $("#current_group").append("<option value='" + strs[i]+ "'>" +strs[i]+"</option>");
                };
            };

        });
    });


    $("#add_user").click(function(){
        var user_list = $("#user_list").val();
        var project = $("#current_user").attr("project");
        var status = $("#current_user").attr("status");

        $.post("/ajax/unique_user_add/", {user_list:user_list, status:status, project:project}, function(data){
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