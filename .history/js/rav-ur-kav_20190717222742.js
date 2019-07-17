
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
    $().on("click", () => {
      $("#recommended-plan").css("display", "flex");
  });
});



$('#rav-kav-number').on('input', function (event) { 
    this.value = this.value.replace(/[^0-9]/g, '');
});

$('.carousel').carousel({
    interval: false
  }).on('slid.bs.carousel', function () {
      curSlide = $('.active');
    if(curSlide.is( ':first-child' )) {
       $('.left').hide();
       return;
    } else {
       $('.left').show();   
    }
    if (curSlide.is( ':last-child' )) {
       $('.right').hide();
       return;
    } else {
       $('.right').show();      
    }
  });