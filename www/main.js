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
});