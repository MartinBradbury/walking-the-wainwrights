/**
 * This Js code has been taken from the Cloudinary website tutorial to allow the 
 * cloudinary widget to be used when upload images.
 */

var myWidget = cloudinary.createUploadWidget({
    cloudName: 'dpjdwg51y',
    uploadPreset: 'user_image'
}, (error, result) => {
    if (!error && result && result.event === "success") {
        document.getElementById('id_feature_img').value = result.info.secure_url;
    }
});

document.getElementById("upload_widget_opener").addEventListener("click", function () {
    myWidget.open();
}, false);