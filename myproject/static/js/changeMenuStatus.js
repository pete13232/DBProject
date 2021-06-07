$(".changeStatus").on("click", function (e) {
  let value = $(this).data("value");
  $.ajax({
    url: "url",
    type: "POST",
    data: { rating: value },
    success: function (d) {
      // some processing
    },
  });
});
