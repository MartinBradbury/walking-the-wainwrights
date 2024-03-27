
    var myWidget = cloudinary.createUploadWidget({
         cloudName: 'dpjdwg51y',
         uploadPreset: 'user_image'}, (error, result) => {
             if (!error && result && result.event === "success") {
                 // Update the feature_img field with the Cloudinary URL
                 document.getElementById('id_feature_img').value = result.info.secure_url;
             }
         }
    );
   
    document.getElementById("upload_widget_opener").addEventListener("click", function(){
         myWidget.open();
    }, false);