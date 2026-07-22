// ----------------------------
// Configuration
// ----------------------------

const SESSION_TIMEOUT = 2 * 60 * 60 * 1000;
const WARNING_BEFORE = 5 * 60 * 1000;

let warningTimer;
let logoutTimer;
let countdownTimer;

// ----------------------------

function resetTimers() {

    clearTimeout(warningTimer);
    clearTimeout(logoutTimer);
    clearInterval(countdownTimer);

    warningTimer = setTimeout(
        showWarning,
        SESSION_TIMEOUT - WARNING_BEFORE
    );

}

// ----------------------------

function showWarning() {

    const modal = new bootstrap.Modal(
        document.getElementById("sessionTimeoutModal")
    );

    modal.show();

    let seconds = 300;

    updateCountdown(seconds);

    countdownTimer = setInterval(() => {

        seconds--;

        updateCountdown(seconds);

        if (seconds <= 0) {

            clearInterval(countdownTimer);

        }

    }, 1000);

    logoutTimer = setTimeout(() => {

        window.location.href = "/portal/logout/";

    }, WARNING_BEFORE);

}

// ----------------------------

function updateCountdown(seconds) {

    const minutes = Math.floor(seconds / 60);

    const secs = seconds % 60;

    document.getElementById("countdown").innerHTML =
        `${String(minutes).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;

}

// ----------------------------

function stayLoggedIn() {

    fetch("/portal/keep-alive/", {

        credentials: "same-origin"

    });

    clearTimeout(logoutTimer);
    clearInterval(countdownTimer);

    bootstrap.Modal
        .getInstance(
            document.getElementById("sessionTimeoutModal")
        )
        .hide();

    resetTimers();

}

// ----------------------------

[
    "click",
    "mousemove",
    "keydown",
    "scroll",
    "touchstart"
].forEach(event => {

    document.addEventListener(
        event,
        resetTimers,
        true
    );

});

document
    .getElementById("stayLoggedIn")
    .addEventListener(
        "click",
        stayLoggedIn
    );

resetTimers();