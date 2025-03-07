document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("translator-form");
    const textArea = document.getElementById("text");

    form.addEventListener("submit", function (event) {
        if (textArea.value.trim() === "") {
            alert("Please enter some text to translate.");
            event.preventDefault();
        }
    });
});