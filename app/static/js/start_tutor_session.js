/*
 * filename: startTutorSession.js
 * author: Angelina Li
 * last modified: 05/13/2018
 * description: adding handlers to index page
 */

$(document).ready( function () {

  $("#course").on("change", function() {
    var course = $(this).find(":selected").text();
    $("#courseName").text(course);
  });
  
  $("input[type=checkbox]").on("change", function() {
    if($(this).is(":checked")) {
      $(this).val(true);
    } else {
      $(this).val(false);
    }
  });

});
