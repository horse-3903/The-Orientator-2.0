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