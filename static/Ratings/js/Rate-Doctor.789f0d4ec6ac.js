// let s1vals = [];
// let s1animals = ["🐬","🐢","🐷","🦁"];
// let slider = new RangeSliderPips({
//   target: document.getElementById("slider2"),
//   props: {
//     min: 0,
//     max: 100,
//     range: true,
//     pushy: false,
//     values: [0],
//     step: 2,
//     pips: true,
//     pipstep: 1,
//     float: true,
//     all: "label",
//     suffix: "%"
//   }
// });

// let slider2 = new RangeSliderPips({
//   target: document.getElementById("slider2"),
//   props: {
//     min: 0,
//     max: 100,
//     range: true,
//     pushy: false,
//     values: [0],
//     step: 2,
//     pips: true,
//     pipstep: 1,
//     float: true,
//     all: "label",
//     suffix: "%"
//   }
// });


// let slider1 = new RangeSliderPips({
//   target: document.getElementById("slider2"),
//   props: {
//     min: 0,
//     max: 100,
//     range: true,
//     pushy: false,
//     values: [0],
//     step: 2,
//     pips: true,
//     pipstep: 1,
//     float: true,
//     all: "label",
//     suffix: "%"
//   }
// });
// // *********************************************

// let $btn = document.querySelector(".s1btn");
// let $s21 = document.querySelector(".s21");
// let $s22 = document.querySelector(".s22");

// // slider 1 bindings

// function setHandles(e) {
//   let labels = e.detail.values;
//   let handles = document.querySelectorAll(".rangeHandle");
//   let handle = document.getElementById("slider").querySelectorAll(".rangeHandle.active");
//   Array.prototype.forEach.call(handles,(el,i)=> {
//     el.children[0].innerHTML = labels[i] + s1animals[i];
//   });
//   s1vals = e.detail.values;
// }
// slider.$on('change', setHandles);
// setHandles({ detail: { values: s1vals }});

// $btn.addEventListener( "click", function() {
//   $btn.innerText = "the values are: " + s1vals;
//   setTimeout(() => {
//     $btn.innerText = "Get Values";
//   }, 1500 );
// })

// // slider 2 bindings 

// // .$on() is a svelte component function
// // https://svelte.dev/docs#$on
// slider.$on('change', function(e) {
//   $s22.value = e.detail.values[0];
// });

// slider2.$on('change', function(e) {
//   $s21.value = e.detail.values[0];
// });
// // .set() is a svelte component function
// // https://svelte.dev/docs#$set
// $s21.addEventListener("change", (e) => {
//   slider2.$set({ values: [ $s21.value, $s22.value ]});
// });

// $s22.addEventListener("change", (e) => {
//   slider2.$set({ values: [ $s21.value, $s22.value ]});
// });


// var max = 10, // Set max value
// initvalue = 0, // Set the initial value
// icon = "fa fa-medkit", // Set the icon (https://fontawesome.com/icons)
// target = document.querySelectorAll('[data-value]'),
// listIcon = document.getElementById("labels-list");

//   // Function to update du value

//   function updateValue(target, value){
//     target.forEach(function(currentIndex) {
//       currentIndex.dataset.value =  value;
//     });
//   }

//   // Init the number of item with the initial value settings

//   for (i = 0; i < max; i++) { 
//     var picto = "<i class='fas "+ icon +"'></i>";
//     $(".labels").append(picto);
//   }

//   updateValue(target, initvalue);

//   // Update the slider on click

//   $('.fas').on( "click", function(){
//     var index = $(this).index() + 1;
//     $( "#range-slider" ).slider( "value", index );
//     updateValue(target, index);
//   });


//   // Init the slider

//   $( "#range-slider" ).slider({
//     range: "min",
//     value: initvalue,
//     min: 0, 
//     max: max, 

//     slide: function( event, ui ) {                     
//       updateValue(target, ui.value);
//     }
//   });





var max = 10, // Set max value
initvalue = 2, // Set the initial value
icon = "fa fa-medkit", // Set the icon (https://fontawesome.com/icons)
target = document.querySelectorAll('[data-value]'),
listIcon = document.getElementById("labels-list");

  // Function to update du value

  function updateValue(target, value){
    target.forEach(function(currentIndex) {
      currentIndex.dataset.value =  value;
    });
  }

  // Init the number of item with the initial value settings

  for (i = 0; i < max; i++) { 
    var picto = "<i class='fas "+ icon +"'></i>";
    $(".labels").append(picto);
  }

  updateValue(target, initvalue);

  // Update the slider on click

  $('.fas').on( "click", function(){
    var index = $(this).index() + 1;
    $( "#range-slider" ).slider( "value", index );
    updateValue(target, index);
  });


  // Init the slider

  $( "#range-slider" ).slider({
    range: "min",
    value: initvalue,
    min: 0, 
    max: max, 

    slide: function( event, ui ) {                     
      updateValue(target, ui.value);
    }
  });






  




