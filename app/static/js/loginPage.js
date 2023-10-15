//The code snippet manipulates a checkbox and a text element using their IDs.
var checkbox = document.getElementById("form2Example31");
var textElement = document.getElementById("rememberMe");
document.getElementById("form2Example31").checked = true;

textElement.style.marginLeft = "-4.8rem";
checkbox.style.marginLeft = "-9.3rem";

checkbox.addEventListener("click", function () {
  if (checkbox.checked) {
    textElement.innerText = "forget Me";
    textElement.style.marginLeft = "-4.8rem";
    checkbox.style.marginLeft = "-9.3rem";
  } else {
    textElement.innerText = "remember Me";
    textElement.style.marginLeft = "-3.5rem";
    checkbox.style.marginLeft = "-7.9rem";
  }
});
