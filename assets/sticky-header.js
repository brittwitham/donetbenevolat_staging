if (!window.dash_clientside) {
  window.dash_clientside = {};
}

window.dash_clientside.clientside = {
  stickyHeader: function (id) {
    var header = document.getElementById("sticky");
    var sticky = header.offsetTop;

    window.onscroll = function () {
      if (window.pageYOffset > sticky) {
        header.classList.add("sticky");
      } else {
        header.classList.remove("sticky");
      }
    };

    return window.dash_clientside.no_update;
  },
};
// window.dash_clientside = Object.assign({}, window.dash_clientside, {
//   clientside: {
//     test_function: function () {
//     //   return someTransform(largeValue1, largeValue2);
//       return alert('If you see this alert, then your custom JavaScript script has run!')
//     },
//   },
// });

// window.addEventListener("load", function () {
//   // document.addEventListener("DOMContentLoaded", function () {
//   // When the event DOMContentLoaded occurs, it is safe to access the DOM

//   // When the user scrolls the page, execute myFunction
//   //   window.addEventListener("scroll", myFunctionForSticky);

//   // Get the navbar
//   var dropdown = document.getElementById("sticky");
//   var sticky = dropdown.offsetTop;

//   // Add the sticky class to the navbar when you reach its scroll position.
//   // Remove "sticky" when you leave the scroll position

//   function myFunctionForSticky() {
//     if (window.pageYOffset >= sticky) {
//       console.log("window.pageYOffset >= sticky");
//     } else {
//       console.log("Not window.pageYOffset >= sticky");
//     }
//     if (window.pageYOffset >= sticky) {
//       dropdown.classList.add("sticky");
//     } else {
//       dropdown.classList.remove("sticky");
//     }
//   }

//   /*Toggle between adding and removing the "responsive" class to topnav
//     when the user clicks on the icon*/

//   function myFunctionForResponsive() {
//     dropdown.classList.toggle("responsive");
//   }
// });
