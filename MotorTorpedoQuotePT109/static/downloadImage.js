var canvas = document.getElementById("canvas");
btnDownload = document.getElementById("downloader");
const imageConverted = document.querySelector("#imageConverted")
btnDownload.addEventListener("click", function() {
    const imageURI = canvas.toDataURL("image/jpeg");
    imageConverted.src = imageURI;
})