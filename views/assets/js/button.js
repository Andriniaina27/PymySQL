const btn = document.getElementById("menu-btn");
const sidebar = document.getElementById("sidebar");

btn.addEventListener("click", function () {
      // bascule la classe active
    sidebar.classList.toggle("active");
});

