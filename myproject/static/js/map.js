var map = document.getElementById("map").innerHTML;
console.log(map);
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    map.innerHTML = "Geolocation is not supported by this browser.";
  }
}
function showError(error) {
  switch (error.code) {
    case error.PERMISSION_DENIED:
      map.innerHTML = "User denied the request for Geolocation.";
      break;
    case error.POSITION_UNAVAILABLE:
      map.innerHTML = "Location information is unavailable.";
      break;
    case error.TIMEOUT:
      map.innerHTML = "The request to get user location timed out.";
      break;
    case error.UNKNOWN_ERROR:
      map.innerHTML = "An unknown error occurred.";
      break;
  }
}

function showPosition(lon, lat) {
  var latlon = lon + "," + lat;
  console.log(latlon);
  var img_url =
    "https://maps.googleapis.com/maps/api/staticmap?center=" +
    latlon +
    "&zoom=14&size=400x300&sensor=false&key=AIzaSyDNbYfnFMJKjvqU3ebFjb-vtJI1K6brJ5k";

  x = document.getElementById("mapholder").innerHTML =
    "<img src='" + img_url + "'>";
  console.log(x);
}
