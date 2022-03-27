btnDownload = document.getElementById("downloader");
btnDownload.addEventListener("click", function() {
    if (window.navigator.msSaveBlob) {
        window.navigator.msSaveBlob(canvas.msToBlob(), "ComedicJoke.png");
    } else {
        const a = document.createElement("a");
        document.body.appendChild(a);
        a.href=canvas.toDataURL();
        a.download = "ComedicJoke.png";
        a.click();
        document.body.removeChild(a);
    }
})