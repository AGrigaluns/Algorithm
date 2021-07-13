
document.addEventListener("DOMContentLoaded", function (event) {
  var acc = document.getElementsByClassName("accordion");
  var i;

  console.log(acc);

  for (i = 0; i < acc.length; i++) { console.log(i);
    acc[i].addEventListener("click", function () {
      this.classList.toggle("active");
      var panel = this.nextElementSibling;
      if (panel.style.maxHeight) {
        panel.style.maxHeight = null;
      } else {
        panel.style.maxHeight = panel.scrollHeight + "px";
      }
    });
  }
});

