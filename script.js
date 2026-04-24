let token = 0;
let current = 0;

let userName = "";
let userPhone = "";

function getToken() {
    userName = document.getElementById("name").value;
    userPhone = document.getElementById("phone").value;

    if (userName === "" || userPhone === "") {
        alert("Enter name & phone");
        return;
    }

    token++;
    document.getElementById("token").innerText = "A" + token;

    updateWait();
}

function nextToken() {
    current++;
    document.getElementById("current").innerText = "A" + current;

    updateWait();
    checkTurn();
}

function updateWait() {
    let diff = token - current;
    let wait = diff * 2;

    if (wait < 0) wait = 0;

    document.getElementById("wait").innerText = wait + " mins";

    document.getElementById("notify").innerText = aiPrediction(diff);
}

function aiPrediction(diff) {
    if (diff <= 0) {
        return "No waiting. You can proceed immediately.";
    }

    let wait = diff * 2;

    return "Estimated waiting time: " + wait +
           " minutes (" + diff + " people × 2 minutes).\n" +
           "Suggested arrival time: In " + wait + " minutes.";
}

function checkTurn() {
    if (token === current) {

        console.log("Sending request...");

        document.getElementById("notify").innerText += 
        "\n🔔 It's your turn, " + userName + "!";

        fetch("/send", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: "phone=" + userPhone
        })
        .then(res => res.text())
        .then(data => console.log("SUCCESS:", data))
        .catch(err => console.error("ERROR:", err));
    }
}