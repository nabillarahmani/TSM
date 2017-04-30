/*function onReady(callback) {
    var intervalID = window.setInterval(checkReady, 1000);

    function checkReady() {
        if (document.getElementsByTagName('body')[0] !== undefined) {
            window.clearInterval(intervalID);
            callback.call(this);
        }
    }
}

function show(id, value) {
    document.getElementById(id).style.display = value ? 'block' : 'none';
}

onReady(function () {
    show('loading', false);
    show('container_page', true);
});*/

function main() {
    setTimeout(function() {
        document.getElementById('loading').className = 'not_loadded';
        document.getElementById('container_page').className = 'loaded';
        setTimeout(function() {
            document.getElementById('loading').className = 'finished';            
        }, 1000);
    }, 2000);
}

window.onload = main();