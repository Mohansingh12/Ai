function detectFakeNews() {
    var userInput = document.getElementById("news_article").value;

    if (userInput.trim() === "") {
        alert("Please enter a news article.");
        return;
    }

    var resultEl = document.getElementById("result_message");
    if (!resultEl) {
        resultEl = document.createElement("div");
        resultEl.id = "result_message";
        resultEl.style.marginTop = "12px";
        document.getElementById("form").appendChild(resultEl);
    }

    resultEl.textContent = "Checking...";

    fetch("/api/get_answer", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: userInput })
    })
        .then(function (res) { return res.json(); })
        .then(function (data) {
            if (data && data.answer) {
                resultEl.textContent = data.answer;
            } else if (data && data.error) {
                resultEl.textContent = "Error: " + data.error;
            } else {
                resultEl.textContent = "Unexpected response.";
            }
        })
        .catch(function (err) {
            resultEl.textContent = "Network error: " + err;
        });
}