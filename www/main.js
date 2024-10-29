$(document).ready(function () {
    

    $('.text').textillate({

        loop : true,
        sync : true,
        in : {
            effect : "bounceIn",
        },
        out : {
            effect : "bounceOut",
        },
    });

    // Siri Wave
    var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style : "ios9",
    amplitude : "1",
    speed : "0.30",
    autostart : true,
    });

    // CortexX message Animation 

    $('.cortexX-message').textillate({

        loop : true,
        sync : true,
        in : {
            effect : "fadeInUp",
            sync : true,
        },
        out : {
            effect : "fadeOutUp",
            sync : true,
        },
    });

    // Mic Click Animation

    $("#MicBtn").click(function () { 
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true );
        $("#SiriWave").attr("hidden", false );
        eel.AllCommands()()
    });


    // Creating keyboard shortcut to make our ai run.

    function DocKeyUp(e){
        if( e.key === 'c' && e.metaKey ){
            eel.playAssistantSound()
            $("#Oval").attr("hidden", true );
            $("#SiriWave").attr("hidden", false );
            eel.AllCommands()()
            
        }
    }
    document.addEventListener('keyup', DocKeyUp , false);

    // Creating function for chat feature

    function PlayAssistant (message) { 
        if (message != ""){
            $("#Oval").attr("hidden", true );
            $("#SiriWave").attr("hidden", false );
            eel.AllCommands(message);
            $("#Chatbox").val("");
            $("#MicBtn").attr("hidden", false );
            $("#SendBtn").attr("hidden", true );

        }
    }

    function ShowHideBtn (message) {
        if(message.length == 0){
            $("#MicBtn").attr("hidden", false );
            $("#SendBtn").attr("hidden", true );
        }
        else{
            $("#MicBtn").attr("hidden", true );
            $("#SendBtn").attr("hidden", false );
        }
    }
    $("#Chatbox").keyup(function () {
        let message =  $("#Chatbox").val();
        ShowHideBtn(message) 
    });
    $("#SendBtn").click(function () { 

        let message =  $("#Chatbox").val();
        PlayAssistant(message)
        
    });

    // Adding the function to also accept message from enter key.
    $("#Chatbox").keypress(function (e) { 
        key = e.which;
        if ( key == 13 ){
            let message =  $("#Chatbox").val();
            PlayAssistant(message)
        }
        
    });
});

