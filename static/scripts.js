window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementById("navbar").style.padding = "0px";
    document.getElementById("navbar").style.backgroundColor = "var(--grey)";
    document.getElementById("navbar-right").style.padding = "5px 10px";
    document.getElementById("logo-image").style.height = "40px";
  } else {
    document.getElementById("navbar").style.padding = "15x 10px";
    document.getElementById("navbar").style.backgroundColor = "transparent";
    document.getElementById("navbar-right").style.padding = "30px 10px";
    document.getElementById("logo-image").style.height = "75px";
  }
  if (document.body.scrollTop > 280 || document.documentElement.scrollTop > 280) {
    document.getElementById("today").style.opacity = "1.0";
  } else {
    document.getElementById("today").style.opacity = "0";
  }
  if (document.body.scrollTop > 550 || document.documentElement.scrollTop > 550) {
    document.getElementById("subscribe").style.opacity = "1.0";
  } else {
    document.getElementById("subscribe").style.opacity = "0";
  }
}
