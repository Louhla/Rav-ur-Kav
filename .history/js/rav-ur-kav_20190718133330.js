
$(document).ready(() => {
  // Globals

  // Modal buttons
  let howToButton = $("#how-to");
  let closeModalButton = $("#close");
  $(closeModalButton).on("click", () => {
    $("#modal-wrapper").toggle();
  });
  $(howToButton).on("click", () => {
    $("#modal-wrapper").toggle();
  });
  // Rav my Kav button
  let reccomendedPlanButton1 = $("#rav-kav-number-button");
  let reccomendedPlanButton2 = $("#rav-my-kav");
  $(reccomendedPlanButton1).on("click", (e) => {
        event.preventDefault();
    $("#recommended-plan").css("display", "flex");
    var randomNumb = Math.floor(Math.random() * 11);;
    $(`#plan${randomNumb}`).css("display", "flex");
  });
  $(reccomendedPlanButton2).on("click", () => {
    $("#recommended-plan").css("display", "flex");
  });
  $("#add-city").on("click", () => {
    $("#hidden-cities").css("display", "flex");
  });
  // $("#rav-kav-number-button").on("click", (function () {
  //   event.preventDefault();
  //   var userRavKavNumber = $("#rav-kav-number").val();
  //   $.ajax({
  //       type: "POST",
  //       url: "localhost7000/",
  //       data: {
  //           ravkavnumber: userRavKavNumber,
  //       },
  //   });
});



  $('#plan-calculator-form1').click(function(){
    var usertype = $("input[name=radio]:checked", "#plan-calculator-form1").val();
      console.log(usertype);
  })
  $('#plan-calculator-form2').click(function(e){
    event.preventDefault();
    var objVal = {};
    var city = $("#plan-calculator-form2").find(":selected").val();
      console.log(city);
  })

//this could be another option:
  // $('#add').on("click", function() {
  //   var objVal = {};
  //   $('select').each(function() {
  //     var arr = $(':selected', this).map(function() {
  //       return this.value;
  //     }).get();
  //     objVal[$(this).attr("name")] = arr;
  //   });
  //   console.log(objVal);
  // });

  $('#plan-calculator-form3').click(function(){
    var frequency = $('#plan-calculator-form3').attr("id", "c2c");
      console.log(frequency);
  })


$('#rav-kav-number').on('input', function (event) {
  this.value = this.value.replace(/[^0-9]/g, '');
});

$('.carousel').carousel({
  interval: false
}).on('slid.bs.carousel', function () {
  curSlide = $('.active');
  if (curSlide.is(':first-child')) {
    $('.left').hide();
    return;
  } else {
    $('.left').show();
  }
  if (curSlide.is(':last-child')) {
    $('.right').hide();
    return;
  } else {
    $('.right').show();
  }
});