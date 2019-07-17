
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



$('#rav-kav-number').on('input', function (event) { 
    this.value = this.value.replace(/[^0-9]/g, '');
});