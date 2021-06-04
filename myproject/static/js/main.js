console.log("Hello World");

const categoryTitle = document.querySelectorAll(".category-title");
const allCategoryPosts = document.querySelectorAll(".All");

for (let i = 0; i < categoryTitle.length; i++) {
  categoryTitle[i].addEventListener(
    "click",
    filterPosts.bind(this, categoryTitle[i])
  );
}

function filterPosts(item) {
  changeActivePosition(item);
  for (let i = 0; i < allCategoryPosts.length; i++) {
    if (allCategoryPosts[i].classList.contains(item.attributes.id.value)) {
      allCategoryPosts[i].style.display = "block";
    } else {
      allCategoryPosts[i].style.display = "none";
    }
  }
}

function changeActivePosition(activeItem) {
  for (let i = 0; i < categoryTitle.length; i++) {
    categoryTitle[i].classList.remove("active");
  }
  activeItem.classList.add("active");
}

$(document).ready(function () {
  $("#myInput").on("keyup", function () {
    // console.log("input1");
    var value = $(this).val().toLowerCase();
    $("#myTable tr").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });

  $("#myInput2").on("keyup", function () {
    // console.log("input2");
    var value = $(this).val().toLowerCase();
    $("#myTable2 tr").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
});
