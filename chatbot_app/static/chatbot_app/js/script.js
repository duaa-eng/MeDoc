// script.js
function getUserInput(){
    var userText = $('#textInput').val();
    var userHTML = "<p class='userText'>User: <span>"+userText+"</span></p>";
    
    $('#textInput').val("");
    $('#chat-container').append(userHTML);

    // Scroll to the bottom
    $('#chat-container').animate({ scrollTop: $('#chat-container')[0].scrollHeight }, 500);

    // Make an ajax request to send user text to the backend python server
    $.get('chatbot/getResponse', { userMessage: userText }).done(function(data){
        var returnedResponse = "<p class='botText'>Chatbot: <span>"+data+"</span></p>";
        $('#chat-container').append(returnedResponse);

        // Scroll to the bottom
        $('#chat-container').animate({ scrollTop: $('#chat-container')[0].scrollHeight }, 500);
    });
}
