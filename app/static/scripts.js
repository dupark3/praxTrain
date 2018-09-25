window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementById("navbar").style.padding = "0px";
    document.getElementById("navbar-right").style.padding = "5px 10px";
    document.getElementById("logo-image").style.height = "40px";
  } else {
    document.getElementById("navbar").style.padding = "0.5em";
    document.getElementById("navbar-right").style.padding = "30px 10px";
    document.getElementById("logo-image").style.height = "75px";
  }
}
/*  if (document.body.scrollTop > 0 || document.documentElement.scrollTop > 0) {
    document.getElementById("today").style.opacity = "1.0";
  } else {
    document.getElementById("today").style.opacity = "0";
  }
  if (document.body.scrollTop > 650 || document.documentElement.scrollTop > 650) {
    document.getElementById("subscribe").style.opacity = "1.0";
  } else {
    document.getElementById("subscribe").style.opacity = "0";
  }*/


function classToggle() {
  const navs = document.querySelectorAll('.navbar-item')  
  navs.forEach(nav => nav.classList.toggle('navbar-toggle-show'));
}

document.querySelector('.navbar-link-toggle')
  .addEventListener('click', classToggle);
