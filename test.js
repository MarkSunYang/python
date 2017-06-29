var page = require('webpage').create();
page.open('http://music.163.com/', function(status) {
  console.log("Status: " + status);
  if(status === "success") {
    page.render('music.png');
  }
  phantom.exit();
});