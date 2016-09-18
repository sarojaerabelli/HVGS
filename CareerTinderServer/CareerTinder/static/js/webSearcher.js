var kairos = new Kairos("188bc00d", "8f75c1508b57e341b4f0a0a57db1fe79");


function addAllNewPictures(gallery_id) {
	listAllSubjectsOfGallery(gallery_id);
}

function addNewPicture(image, subject_id, gallery_id) {
    // (1) set up your callback method
    function myDetectCallback(response) {
        console.log(response.responseText);
    }

    // (2) prepare your parameters  
    // var base64_data = 'iVBORw0KGgoAAA ... ABJRU5ErkJggg==\r\n';
    // var subject_id  = 'eric';
    // var gallery_id  = 'friends1';
    // var base64_data = toDataURL(image);

    var base64_data = toDataUrl(image, function(base64Img) {
        kairos.enroll(base64Img, gallery_id, subject_id, myDetectCallback);
    });



    // (3) pass your params and callback to the function
    // kairos.enroll(base64_data, gallery_id, subject_id, myDetectCallback);
}

function matchImageToPerson(image, gallery_id) {
    // (1) set up your callback method
    function myDetectCallback(response) {
    	var str = response.responseText;
		var json = JSON.stringify(eval("(" + str + ")"));

		json.images["transaction"].subject;

		var regex = /(\d*)\.\w+/;
		var match = regex.exec(json.images["transaction"].subject);

		window.location = "thumbnails/" + match[1];

        // console.log(response.responseText);
    }

    // (2) prepare your parameters  
    // base64_data = 'iVBORw0KGgoAAA ... ABJRU5ErkJggg==\r\n';
    // gallery_id  = 'friends1';
    // var base64_data = changeToBase64(image);

    // (3) ... as well as any optional parameters you wish to send
    var options = { "threshold": 0.75 };

    // var base64_data = toDataUrl(image, function(base64Img) {
	   //  kairos.recognize(base64Img, gallery_id, myDetectCallback, options);
    // });
    image = image.src.replace(/^data:image\/(png|jpg);base64,/, "")


    // (4) pass your params and callback to the function
    kairos.recognize(image, gallery_id, myDetectCallback, options);
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
    	var str = response.responseText;
		var json = JSON.stringify(eval("(" + str + ")"));

		var listOfIDs = json.subject_ids;

		var imageFolder = '../../../media/media/faces/';
		var imgsrc = "";
		var i = 0;

		imgsrc = imageFolder + i;
		while (UrlExists(imgsrc)) {
			i++;
			if (listOfIDs.indexOf(imgsrc) > -1) {
				addNewPicture(imgsrc, i, gallery_id);
			}
			imgsrc = imageFolder + i;
		}
    }

    // (2) prepare your parameters  
    // var gallery_id = 'friends1';

    // (3) pass your params and callback to the function
    kairos.viewSubjectsInGallery(gallery_id, myDetectCallback);
}


function UrlExists(url) {
    var http = new XMLHttpRequest();
    http.open('HEAD', url, false);
    http.send();
    return http.status != 404;
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

// function changeToBase64(image) {
//     // toDataUrl(image, function(base64Img) {
//     //     return base64Img;
//     // });

//     // toDataUrl(image, function(base64Img) {
//     //     return base64Img;
//     // });

//     return toDataURL(image);


//     // toDataUrl('http://example/url', function(base64Img) {
//     //     console.log(base64Img);
//     // });
// }


function getBase64FromImageUrl(url) {
    var img = new Image();

    img.setAttribute('crossOrigin', 'anonymous');

    img.onload = function() {
        var canvas = document.createElement("canvas");
        canvas.width = this.width;
        canvas.height = this.height;

        var ctx = canvas.getContext("2d");
        ctx.drawImage(this, 0, 0);

        var dataURL = canvas.toDataURL("image/png");

        // alert(dataURL.replace(/^data:image\/(png|jpg);base64,/, ""));

        return (dataURL.replace(/^data:image\/(png|jpg);base64,/, ""));
    };

    img.src = url;
}

function toDataUrl(url, callback) {
    var img = new Image();

    img.setAttribute('crossOrigin', 'anonymous');

    img.onload = function() {
        var canvas = document.createElement("canvas");
        canvas.width = this.width;
        canvas.height = this.height;

        var ctx = canvas.getContext("2d");
        ctx.drawImage(this, 0, 0);

        var dataURL = canvas.toDataURL("image/png");

        // alert(dataURL.replace(/^data:image\/(png|jpg);base64,/, ""));

        callback(dataURL.replace(/^data:image\/(png|jpg);base64,/, ""));
    };

    img.src = url;
}


// function toDataUrl(url, callback) {
//     var xhr = new XMLHttpRequest();
//     xhr.responseType = 'blob';
//     xhr.onload = function() {
//         var reader = new FileReader();
//         reader.onloadend = function() {
//             callback(reader.result);
//         };
//         reader.readAsDataURL(xhr.response);
//     };
//     xhr.open('GET', url);
//     xhr.send();
// }
