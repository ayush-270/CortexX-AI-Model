$(document).ready(function () {
    
    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message){
        $(".cortixX-message li:first").text(message);
        $(".cortixX-message").textillate('start');
    };

    // Displaying the main page again after the process of speech.
    eel.expose(DisplayHood)
    function DisplayHood(){
        $("#Oval").attr("hidden", false );
        $("#SiriWave").attr("hidden", true );
    };

});