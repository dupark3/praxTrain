/*
// SHRINKING STICKY NAVBAR
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementByClassName("navbar").style.height = "100px";
    document.getElementById("logo-image").style.height = "40px";
  } else {
    document.getElementById("navbar").style.padding = "0.5em";
    document.getElementById("navbar-right").style.padding = "30px 10px";
    document.getElementById("logo-image").style.height = "75px";
  }
}
  if (document.body.scrollTop > 0 || document.documentElement.scrollTop > 0) {
    document.getElementById("today").style.opacity = "1.0";
  } else {
    document.getElementById("today").style.opacity = "0";
  }
  if (document.body.scrollTop > 650 || document.documentElement.scrollTop > 650) {
    document.getElementById("subscribe").style.opacity = "1.0";
  } else {
    document.getElementById("subscribe").style.opacity = "0";
  }
*/

// NAVBAR MOBILE MENU
// navbar-link-toggle is the hamburger menu of mobile view,
// other navbar-items toggle to show and not show on click of menu
function classToggle() {
  const navs = document.querySelectorAll('.navbar-item')  
  navs.forEach(nav => nav.classList.toggle('navbar-toggle-show'));
}
document.querySelector('.navbar-link-toggle')
  .addEventListener('click', classToggle);


// SUBSCRIPTION MODAL
// Get the divs
var modal = document.getElementById('myModal');
var btns = document.querySelectorAll(".myBtn");

// When the user clicks the button, open the modal 
for (var i = 0; i < btns.length; i++){
  btns[i].onclick = function() {
      modal.style.display = "block";
  }
}

// Open modal if myBtn clicked. Close modal if clicked outside of modalContent
$(document).ready(function(){
    $('.myBtn').on('click touchstart', function() {
      $('#myModal').css('display','block');
      // Wait until display transition is done to focus
      setTimeout(function(){
          $('#firstNameSub').focus();
      });
    });
    $("#myModal").on('click touchstart', function(close) {
      if (close.target.id == "modal-content" || $(close.target).parents("#modal-content").length) {
        $('#myModal').css('display','block');
      } else {
        $('#myModal').css('display','none');
      }
    });
});

$(window).on("load",function() {
  $(window).scroll(function() {
    var windowBottom = $(this).scrollTop() + $(this).innerHeight();
    $(".fade").each(function() {
      /* Check the location of each desired element */
      var objectBottom = $(this).offset().top + $(this).outerHeight();
      
      /* If the element is completely within bounds of the window, fade it in */
      if (objectBottom < windowBottom) { //object comes into view (scrolling down)
        if ($(this).css("opacity")==0) {$(this).fadeTo(500,1);}
      } else { //object goes out of view (scrolling up)
        if ($(this).css("opacity")==1) {$(this).fadeTo(500,0);}
      }
    });
  }).scroll(); //invoke scroll-handler on page-load
});