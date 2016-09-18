// database holds 
/*
name
date_of_birth
face_picture
resume_picture

Hiree



*/

var kairos = new Kairos("188bc00d", "8f75c1508b57e341b4f0a0a57db1fe79");


function addNewPicture(image, subject_id, gallery_id) {
    // (1) set up your callback method
    function myDetectCallback(response) {
        console.log(response.responseText);
    }

    // (2) prepare your parameters  
    // var base64_data = 'iVBORw0KGgoAAA ... ABJRU5ErkJggg==\r\n';
    // var subject_id  = 'eric';
    // var gallery_id  = 'friends1';
    var base64_data = changeToBase64(image);

    // (3) pass your params and callback to the function
    kairos.enroll(base64_data, gallery_id, subject_id, myDetectCallback);
}

function matchImageToPerson(image, gallery_id) {
    // (1) set up your callback method
    function myDetectCallback(response) {
        console.log(response.responseText);
    }

    // (2) prepare your parameters  
    // base64_data = 'iVBORw0KGgoAAA ... ABJRU5ErkJggg==\r\n';
    // gallery_id  = 'friends1';
    var base64_data = changeToBase64(image);

    // (3) ... as well as any optional parameters you wish to send
    var options = { "threshold": 0.75 };


    // (4) pass your params and callback to the function
    kairos.recognize(image_data, gallery_id, myDetectCallback, options);
}

function listAllGalleries() {
    // (1) set up your callback method
    function myDetectCallback(response) {
        alert(response.responseText);
    }

    // (2) pass your callback to the function
    kairos.viewGalleries(myDetectCallback);
}

function listAllSubjectsOfGallery(gallery_id) {
    // (1) set up your callback method
    function myDetectCallback(response) {
        alert(response.responseText);
    }

    // (2) prepare your parameters  
    // var gallery_id = 'friends1';

    // (3) pass your params and callback to the function
    kairos.viewSubjectsInGallery(gallery_id, myDetectCallback);
}

function removeGallery(gallery_id) {
    // (1) set up your callback method
    function myDetectCallback(response) {
        alert(response.responseText);
    }

    // (2) prepare your parameters  
    // var gallery_id = 'friends1';

    // (3) pass your params and callback to the function
    kairos.removeGallery(gallery_id, myDetectCallback);
}

function removeSubjectFromGallery(subject_id, gallery_id) { // (1) set up your callback method
    function myDetectCallback(response) {
        alert(response.responseText);
    }

    // (2) prepare your parameters  
    // var subject_id = 'sam';
    // var gallery_id = 'friends1';

    // (3) pass your params and callback to the function
    kairos.removeSubjectFromGallery(subject_id, gallery_id, myDetectCallback);
}

function changeToBase64(image) {
    toDataUrl(image, function(base64Img){
    	return base64Img;
    });

    // toDataUrl('http://example/url', function(base64Img) {
    //     console.log(base64Img);
    // });



}

function toDataUrl(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.responseType = 'blob';
    xhr.onload = function() {
        var reader = new FileReader();
        reader.onloadend = function() {
            callback(reader.result);
        };
        reader.readAsDataURL(xhr.response);
    };
    xhr.open('GET', url);
    xhr.send();
}
