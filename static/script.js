// Fonction pour basculer la sidebar sur mobile
function toggleMobileSidebar() {
  const sidebar = document.querySelector(".sidebar");
  sidebar.classList.toggle("show-sidebar");
}

// Ferme la sidebar sur mobile lorsqu'on clique sur un lien
document.querySelectorAll(".sidebar a").forEach((link) => {
  link.addEventListener("click", () => {
    const sidebar = document.querySelector(".sidebar");
    sidebar.classList.remove("show-sidebar");
  });
});
