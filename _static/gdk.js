document.addEventListener('DOMContentLoaded', function() {
    var events = document.getElementsByClassName('event');
    Array.from(events).forEach(function (event) {
        var start = Date.parse(event.getElementsByClassName('event-start')[0].innerText);
        var end = Date.parse(event.getElementsByClassName('event-end')[0].innerText);

        var actualend = event.getElementsByClassName('event-actualend');
        if (actualend.length > 0) {
            var end = Date.parse(event.getElementsByClassName('event-actualend')[0].innerText);
        }

        var now = Date.now();

        var nowSecs = Math.floor(now / 1000);
        var endSecs = Math.floor(end / 1000);
        if (endSecs < nowSecs - 24 * 60 * 60) {
            event.classList.add('status-old');
            return;
        }

        if (now < start) {
            event.classList.add('status-upcoming');
        } else if (now > end) {
            event.classList.add('status-ended');
        } else {
            event.classList.add('status-ongoing');
        }
    });
}, false);
