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

if(current === "contacto") {
  select = document.getElementById("contact-select");
  textarea = document.getElementById("contact-textarea");
  console.log("corre")
  textarea.disabled = true;
  select.onchange = (event) => {
    if (event.target.selectedIndex === 0) {
      textarea.disabled = true;
    }
    else {
      textarea.disabled = false;
    }
  }
}

// if (current === "contacto") {
//   select = document.getElementsByTagName("select");
//   textarea = document.getElementsByTagName("textarea");
//   select.addEventListener();
//   if (select.selectedIndex === 1) {
//     textarea.disabled = true;
//   }
//   else (
//     textarea.disabled = false;
//   )
// }