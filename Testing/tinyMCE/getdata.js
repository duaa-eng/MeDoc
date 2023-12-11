$(document).ready(function() {

    $("#get-data").submit(function(e) {

        var content = tinymce.get("texteditor").getContent();

        // var htmlstr = content.html();
        $("#data-container").text(content);
        // document.getElementById("data-container").innerHTML = content;

        return false;

    })

})

// $("#data-html").click(function () {
//     $("#data-html").html($("#data-container").val());
// })