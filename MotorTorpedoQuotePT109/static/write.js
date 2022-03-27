var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
var img = document.getElementById("picture");
var text = document.getElementById("quote")
canvas.onload
ctx.drawImage(img, -100, 0, 700, 500);
textArray = text.textContent.split("/")
ctx.font = "30px Comic Sans MS";
ctx.fillStyle = "white";
ctx.strokeStyle = "black";
ctx.textAlign = "center";
ctx.fillText(textArray[0], 250, 40);
ctx.strokeText(textArray[0], 250, 40);
ctx.fillText(textArray[1], 250, 80);
ctx.strokeText(textArray[1], 250, 80);
ctx.font = "35pt Calibri";
ctx.fillText(textArray[2], 250, 470);
ctx.strokeText(textArray[2], 250, 470);
const imageURI = canvas.toDataURL("image/jpeg");
imageConverted.src = imageURI;