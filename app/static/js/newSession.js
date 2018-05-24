/*
 * filename: newSession.js
 * author: Angelina Li
 * last modified: 05/13/2018
 * description: JS code for newSession page
 */

$(document).ready( function() {
  
  var validateUserUrl = "/validateUser/";
  var userCoursesUrl = "/getUserCourses/";
  var defaultCourseText = "Select a course";
  var unknownUsernameText = "Unknown username";
  var invalidCourseText = "This user is not taking this course!";

  function renderTemplate(templateSelector, data) {
    /* templateSelector: a jQuery selector representing a mustache template object.
     * data: JSON data to populate the template with.
     * This function will parse & render an object as formatted using the mustache
     * templating engine, populated with the data as specified in data.
     * */
    var template = $(templateSelector).html();
    Mustache.parse(template);
    var rendered = Mustache.render(template, data);
    return rendered;
  }

  function resetSelect(selector, disabledText) {
    /* selector: a jQuery selector representing object(s) of type select.
     * disabledText: text to display as the default disabled select
     *   option.
     * This function will 'reset' the specified selector to its
     * default state (before the user has entered a valid username)
     * */
    $(selector).empty();
    $(selector).attr("readonly", true);
    $(selector).append(
      renderTemplate("#inactive-option-template", {"text": disabledText}));
  }

  function addErrorMessage(selector, errorText, submitSelector) {
    /* selector: a jQuery selector
     * errorText: the error text to display
     * buttonSelector: a jQuery selector representing a button of type submit
     * This function will add an error with text 'errorText' to the
     * specified selector, and disable the submit button specified.
     * */
    $(selector).append(
      renderTemplate("#error-msg-template", {"text": errorText}));
    $(submitSelector).attr("disabled", true);
  }

  function addOption(selector, optionValue, optionText) {
    /* selector: a jQuery selector representing object(s) of type select.
     * optionValue: value for this option to take.
     * optionText: text for this option to display.
     * This function will add an option with value 'optionValue' and
     * text 'optionText' to the specified select object.
     * */
    $(selector).append(
      renderTemplate("#option-template", 
        {"text": optionText, "value": optionValue}));
  }
  
  function addUserCourses(username, dept) {
    /* username: string representing the username supplied by the user.
     * dept: string representing the department this user is selecting 
     *       courses from.
     * This function will retrieve all the courses a user is
     * a part of and will add a course option for each course.
     * */
    $.post(
      userCoursesUrl,
      {"username": username, "dept": dept},
      function (data) {
        var userCourses = data.courses;
        for(i=0; i < userCourses.length; i++) {
          course = userCourses[i];
          addOption("#course", course.cid, course.name);
        }
        $("#course").attr("readonly", false);
      });
  }

  function populateFields(username, autoPop, validateData) {
    /* username: string representing the username supplied by the user.
     * autoPop: boolean == true if this form should be auto populated.
     * validateData: JSON object representing validation data.
     * This function will handle validating the user's request and
     * presenting the relevant courses.
     * */

    $("#username-messages").empty();
    $("#submitNewSession").attr("disabled", false);
    resetSelect("#course", defaultCourseText);

    if (!validateData.validUsername) {
      addErrorMessage("#username-messages", unknownUsernameText, 
        "#submitNewSession");
    } else if (!autoPop) {
      /* if not autoPop, we don't need to check for course validity. */
      addUserCourses(username, $("#dept").val() );
    } else if (!validateData.validCourse) {
      /* if autoPop, we don't need to add user courses; just need to
       * check whether this user is attending a section of the course 
       * specified */
      addErrorMessage("#username-messages", invalidCourseText, 
        "#submitNewSession");
    } else {
      /* if autoPop with a valid username and course, update cid */
      $("#cid").val(validateData.studentCid);
    }
  }

  $("#username").on("input", function (event) {
    var username = $(this).val();
    var cid = $("#cid").val();
    var autoPop = $("#autoPop").val() == "True";
    
    $.post(
      validateUserUrl,
      {"username": username, "cid": cid, "autoPop": autoPop},
      function (data) { populateFields(username, autoPop, data); }
    );
  
  });

});
