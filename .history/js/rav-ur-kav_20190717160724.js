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
      console.log('how to')
    });
});
console.log("whats up")



$('.numeric').on('input', function (event) { 
    this.value = this.value.replace(/[^0-9]/g, '');
});