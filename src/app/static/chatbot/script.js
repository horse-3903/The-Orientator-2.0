const chatForm = document.getElementById("chatForm");
const chatMessages = document.getElementById("chatMessages");
const userInput = document.getElementById("userInput");

chatForm.addEventListener("submit", function (event) {
    event.preventDefault();

    var userMessage = userInput.value.trim();

    if (userMessage) {
        if (userMessage.length > 150){
            const result = [];
            for (let i = 0; i < userMessage.length; i += 100) {
                result.push(userMessage.slice(i, i + 100));
            }
    
            userMessage = result.join("\n")
        }

        // Display user's message aligned to the right
        const userMessageElement = document.createElement("div");
        userMessageElement.className = "message user m-2 px-3 py-2 border rounded bg-primary text-white text-end ms-auto";
        userMessageElement.innerText = userMessage;
        userMessageElement.style = "width: fit-content";
        chatMessages.appendChild(userMessageElement);

        // Scroll to the latest message
        chatMessages.scrollTop = chatMessages.scrollHeight;

        // Clear the input field
        userInput.value = "";

        data = (async () => {
            response = await fetch("/api-route/")
            return await response.json()
        })

        console.log(response)

        const assistantMessageElement = document.createElement("div");
        assistantMessageElement.className = "message chatbot m-2 px-3 py-2 border border-secondary rounded me-auto";
        assistantMessageElement.innerText = "I'm an AI assistant. How can I help you?";
        assistantMessageElement.style = "width: fit-content";
        chatMessages.appendChild(assistantMessageElement);

        // Scroll to the latest message
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});

function modeToggle(element) {
    const label = document.querySelector("label[for='" + element.id + "']");

    if (element.checked) {
        label.innerText = "Dark Mode";
        document.querySelector("html").setAttribute("data-bs-theme", "dark");

        fetch("/api-route/mode-pref", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                mode: "dark"
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Dark mode preference saved:", data);
        })
        .catch(error => {
            console.error("Error saving dark mode preference:", error);
        });

    } else {
        label.innerText = "Light Mode";
        document.querySelector("html").setAttribute("data-bs-theme", "light");

        fetch("/api-route/mode-pref", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                mode: "light"
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Light mode preference saved:", data);
        })
        .catch(error => {
            console.error("Error saving light mode preference:", error);
        });
    }
}