console.log("Hello World");

const fName = document.getElementById("userForm");

console.log(fName);

const url = "";

$(document).ready(function () {
    $("#myInput").on("keyup", function () {
      // console.log("input1");
      var value = $(this).val().toLowerCase();
      $("#myTable tr").filter(function () {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });

    $("#myInput2").on("keyup", function () {
      // console.log("input2");
      var value = $(this).val().toLowerCase();
      $("#myTable2 tr").filter(function () {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });

