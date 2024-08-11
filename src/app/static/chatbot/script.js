const chatForm = document.getElementById("chatForm");
const chatMessages = document.getElementById("chatMessages");
const userInput = document.getElementById("userInput");

chatForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const userMessage = userInput.value.trim();
    if (userMessage) {
        // Display user's message aligned to the right
        const userMessageElement = document.createElement("div");
        userMessageElement.className = "message user m-2 p-2 pe-3 border rounded bg-primary text-white text-end w-50 ms-auto";
        userMessageElement.innerText = userMessage;
        chatMessages.appendChild(userMessageElement);

        // Scroll to the latest message
        chatMessages.scrollTop = chatMessages.scrollHeight;

        // Clear the input field
        userInput.value = "";

        // Simulate assistant's response
        setTimeout(() => {
            const assistantMessageElement = document.createElement("div");
            assistantMessageElement.className = "message chatbot m-2 p-2 ps-3 border border-secondary rounded w-50 me-auto";
            assistantMessageElement.innerText = "I'm an AI assistant. How can I help you?";
            chatMessages.appendChild(assistantMessageElement);

            // Scroll to the latest message
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }, 1000);
    }
});

function modeToggle(element){
    label = document.querySelector("label[for='" + element.id + "']")

    if (element.checked){
        label.innerText = "Dark Mode"
        document.querySelector("html").setAttribute("data-bs-theme", "dark")
    } else {
        label.innerText = "Light Mode"
        document.querySelector("html").setAttribute("data-bs-theme", "light")
    }

}