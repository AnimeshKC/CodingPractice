let colorSpec = document.querySelector("colorSpec");
let color1 = document.querySelector(".color1");
let color2 = document.querySelector(".color2");
let body = document.querySelector("body");

function changeColors() {
  body.style.background = `linear-gradient(to right, ${color1.value}, ${color2.value})`;
  if (colorSpec) colorSpec.textContent = body.style.background;
}
changeColors();
color1.addEventListener("input", changeColors);
color2.addEventListener("input", changeColors);
