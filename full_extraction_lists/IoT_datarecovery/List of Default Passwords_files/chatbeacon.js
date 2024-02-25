var initBeacon = function () {

    var serviceUrl = "";
    var scripts = document.getElementsByTagName("script");
    var url;

    for (var i = 0; i < scripts.length; i++) {
        var js = scripts[i];
        var jssrc = js.src;
        
        if(!jssrc)
            continue;

        var index = jssrc.indexOf("chatbeacon.js");

        if (index > -1) {
            url = jssrc;
            break;
        }
    }

    var index2 = url.indexOf("scripts");
    serviceUrl = index2 > -1 ? url.substr(0, index2) : url;
    if (window.msCrypto) {
        console.log("calling fallback");
        var fallback = document.createElement("script");

        fallback.src = serviceUrl + "scripts/fallback.js";
        document.body.appendChild(fallback);      
    }
    else {
        var beaconScript = document.createElement("script");

        beaconScript.src = serviceUrl + "scripts/main.js?v=6";
        beaconScript.async = true;
        beaconScript.defer = true;
        document.body.appendChild(beaconScript);
    }
};

initBeacon();