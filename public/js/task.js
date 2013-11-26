$(document).ready(function(){
    $("#task_type").change(function(){
        $("#task_project_sl option").remove();
        $("#task_project_sl").prepend("<option value=''>请选择</option>");
        var project = $("#task_type").val();

        $.post("/ajax/get_project/", {project:project}, function(data){
            //alert(data);

            var strs= new Array();
            strs = data.split("|");
            for (var i =0; i<strs.length; i++) {
                if (strs[i]) {
                    $("#task_project_sl").append("<option value='" + strs[i]+ "'>" +strs[i]+"</option>");
                };
            };

        });
    });
});