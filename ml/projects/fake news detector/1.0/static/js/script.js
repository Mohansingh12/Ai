function detectFakeNews()
{
    var userInput = document.getElementById("news_article").value;

    if(userInput.trim() === "")
    {
        alert("Please enter a news article.");
        return;
    }
    else
    {
        fetch()
    }

}