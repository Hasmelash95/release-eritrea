let today = new Date().getFullYear();
const presentYear = document.getElementById('current-year');

presentYear.innerHTML = today;

$('#exampleModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var ajaxUrl = button.data('ajaxurl') // Extract info from data-* attributes
    
    $('#exampleModal-content').load(ajaxUrl)
  })