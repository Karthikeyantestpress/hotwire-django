// This is the scss entry file
import "../styles/turbo_drive.scss";

import "@hotwired/turbo";

window.document.addEventListener("DOMContentLoaded", function () {
  window.console.log("dom ready");
});

document.addEventListener('turbo:load', function () {     // new
  console.log('turbo:load');
});