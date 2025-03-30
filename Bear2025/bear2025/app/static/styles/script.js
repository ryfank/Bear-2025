// =-=-=-=-=-=-=-=-= //
// IMAGE IMPORT CODE //
// =-=-=-=-=-=-=-=-==//
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
// =-=-=-=-=-=-=-= //
// DARK MODE CODE //
// =-=-=-=-=-=-=-= //
let darkmode = localStorage.getItem('darkmode')
const themeSwitch = document.getElementById('darkmode-toggle')

const enableDarkmode = () => {
    document.body.classList.add('darkmode')
    localStorage.setItem('darkmode', 'active')
}

const disableDarkmode = () => {
    document.body.classList.remove('darkmode')
    localStorage.setItem('darkmode', null)
}

if(darkmode === "active") enableDarkmode()

themeSwitch.addEventListener("click", () => {
    darkmode = localStorage.getItem('darkmode')
    darkmode !== "active" ? enableDarkmode() : disableDarkmode()
})
