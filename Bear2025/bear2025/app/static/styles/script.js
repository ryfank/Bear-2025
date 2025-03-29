document.addEventListener("DOMContentLoaded", function () {
    const imageInput = document.getElementById("imageInput");
    const displayImage = document.getElementById("displayImage");

    imageInput.addEventListener("change", function (event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                displayImage.src = e.target.result;
                displayImage.style.display = "block";
            };
            reader.readAsDataURL(file);
        } else {
            displayImage.style.display = "none"; // Hide image if no file selected
            displayImage.src = "";
        }
    });
});
