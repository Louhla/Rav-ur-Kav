console.log("step1");

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
    let reccomendedPlanButton = $("#rav-kav-number-button");
    $(reccomendedPlanButton).on("click", () => {
        $("#recommended-plan").css("display", "flex");
    })
    
});
console.log("whats up")



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