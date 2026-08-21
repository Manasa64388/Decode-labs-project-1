const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");
const navigationItems = document.querySelectorAll(".nav-links a");

menuToggle.addEventListener("click", function () {
    navLinks.classList.toggle("active");

    const isOpen = navLinks.classList.contains("active");

    menuToggle.setAttribute("aria-expanded", isOpen);

    menuToggle.textContent = isOpen ? "✕" : "☰";
});


navigationItems.forEach(function (link) {
    link.addEventListener("click", function () {
        navLinks.classList.remove("active");

        menuToggle.setAttribute("aria-expanded", "false");

        menuToggle.textContent = "☰";
    });
});