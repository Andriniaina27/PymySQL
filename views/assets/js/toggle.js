const menu = document.getElementById("menu-bar");
const nav  = document.getElementById("navlink");

menu.addEventListener("click", function(){
  nav.classList.toggle("active");
});

