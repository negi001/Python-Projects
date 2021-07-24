// set window size
window.onresize = function () {
  if (
    window.outerWidth < 896 ||
    window.outerHeight < 389 ||
    window.outerWidth > 896 ||
    window.outerHeight > 389
  ) {
    window.resizeTo(896, 389);
  }
};

// call python code
function fetchURL(url) {
  var url = document.getElementById("text").value;
  eel.short_url(url)(setURL);
}

// set url
function setURL(url) {
  var textarea = document.getElementById("text1");
  textarea.innerHTML = url;
}
