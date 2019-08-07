$(document).ready(function(){

  $(function() {
    $("#search").autocomplete({
      source: "{% url 'ajax_load_project' %}",
      minLength: 2,
    });
  });

});
