// toggles class active
const navbar = document.querySelector(".navbar-nav");
// ketika hamburger menu di klik
document.querySelector("#hamburger-menu").onclick = () => {
  navbar.classList.toggle("active");
};

// klik diluar sidebar unutuk menghilangkan nav nya
const hamburger = document.querySelector("#hamburger-menu");
document.addEventListener("click", function (e) {
  if (!hamburger.contains(e.target) && !navbar.contains(e.target)) {
    navbar.classList.remove("active");
  }
});
