$(document).ready(function() {
  $("#compress-btn").click(function() {
      var inputText = $("#input-text").val();
      $.ajax({
          type: "POST",
          url: "/compress",
          data: {text: inputText},
          success: function(response) {
              $("#output-text").val(response);
          }
      });
  });

  $("#decompress-btn").click(function() {
      var inputText = $("#input-text").val();
      $.ajax({
          type: "POST",
          url: "/decompress",
          data: {text: inputText},
          success: function(response) {
              $("#output-text").val(response);
          }
      });
  });
});
