let current = window.location.href;
current = current.replace(/^https?:\/\//, "").split("/")[1];
if (current !== "") {
  let linkList = document.getElementsByClassName("nav-link");
  for (let link of linkList) {
    link.classList.remove("active");
    if (current === "edificios" && link.id === "properties-link") {
      link.classList.add("active");
    } else if (current === "contacto" && link.id === "contact-link") {
      link.classList.add("active");
    } else if (current === "acerca" && link.id === "about-link") {
      link.classList.add("active");
    } else if (current === "cuenta" && link.id === "login-link") {
      link.classList.add("active");
    }
  }
}
