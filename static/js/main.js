
const contactBtn = document.getElementById("contact-btn");
contactBtn.addEventListener("click",() => {
    console.log("triggered")
    $("#about-me-div").slideToggle();
    aboutMeDiv = document.getElementById("about-me-div");
    aboutMeDiv.style.display = 'block'
    aboutMeDiv.style.position= 'relative'
})