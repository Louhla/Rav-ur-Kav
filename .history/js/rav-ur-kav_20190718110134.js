
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
  $(reccomendedPlanButton1).on("click", () => {
    $("#recommended-plan").css("display", "flex");
  });
  $(reccomendedPlanButton2).on("click", () => {
    $("#recommended-plan").css("display", "flex");
  });
  $("#add-city").on("click", () => {
    $("#hidden-cities").css("display", "flex");
  });
  $('#rav-kav-number-button').click(function(){
    var userRavKavNumber = $("#rav-kav-number").val();
      console.log(userRavKavNumber);
  })
  $('#plan-calculator-form1').click(function(){
    var usertype = $("input[name=radio]:checked", "#plan-calculator-form1").val();
      console.log(usertype);
  })
  $('#plan-calculator-form2').click(function(){
    var city = $("#plan-calculator-form2").find(":selected").val();
      console.log(city);
  })
  $('#plan-calculator-form3').click(function(){
    var frequency = $('#plan-calculator-form3').attr(id").val();
      console.log(frequency);
  })
});


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