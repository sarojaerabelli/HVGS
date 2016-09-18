'''
ok so what's going to happen is that a picture is going to be snapped
that picture is going to be saved into the database with a url
and then I can pass that url into the API call along with a looping over of all the rest of the database pictures

also, once a picture is snapped, save it into a taken picture database versus the actual uploaded picture database
then...get the returned value of all of those function calls, if one is true, match that info

if true:
	get the name and search facebook and linkedin and more...
	parse out info or something? and then return the urls and relevant id number in database to another thing

if false:
	delete from taken picture database


also make a method that takes all those relevant urls and id number to display things on the web app
'''


import time 
import requests
import cv2
import operator
import numpy as np
from __future__ import print_function

# Import library to display results
# import matplotlib.pyplot as plt
# %matplotlib inline 
# Display images within Jupyter

# Variables

_url = 'https://api.projectoxford.ai/face/v1.0/detect'
_key = '601f4511257c43539ee336fcef625558' #Here you have to paste your primary key
_maxNumRetries = 5


def processRequest( json, data, headers, params ):

    """
    Helper function to process the request to Project Oxford

    Parameters:
    json: Used when processing images from its URL. See API Documentation
    data: Used when processing image read from disk. See API Documentation
    headers: Used to pass the key information and the data type request
    """

    retries = 0
    result = None

    while True:

        response = requests.request( 'post', _url, json = json, data = data, headers = headers, params = params )

        if response.status_code == 429: 

            print( "Message: %s" % ( response.json()['error']['message'] ) )

            if retries <= _maxNumRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                print( 'Error: failed after retrying!' )
                break

        elif response.status_code == 200 or response.status_code == 201:

            if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                result = None 
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                if 'application/json' in response.headers['content-type'].lower(): 
                    result = response.json() if response.content else None 
                elif 'image' in response.headers['content-type'].lower(): 
                    result = response.content
        else:
            print( "Error code: %d" % ( response.status_code ) )
            print( "Message: %s" % ( response.json()['error']['message'] ) )

        break
        
    return result


def renderResultOnImage( result, img ):
    
    """Display the obtained results onto the input image"""

    for currFace in result:
        faceRectangle = currFace['faceRectangle']
        cv2.rectangle( img,(faceRectangle['left'],faceRectangle['top']),
                           (faceRectangle['left']+faceRectangle['width'], faceRectangle['top'] + faceRectangle['height']),
                       color = (255,0,0), thickness = 1 )

        faceLandmarks = currFace['faceLandmarks']

        for _, currLandmark in faceLandmarks.items():
            cv2.circle( img, (int(currLandmark['x']),int(currLandmark['y'])), color = (0,255,0), thickness= -1, radius = 1 )

    for currFace in result:
        faceRectangle = currFace['faceRectangle']
        faceAttributes = currFace['faceAttributes']

        textToWrite = "%c (%d)" % ( 'M' if faceAttributes['gender']=='male' else 'F', faceAttributes['age'] )
        cv2.putText( img, textToWrite, (faceRectangle['left'],faceRectangle['top']-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1 )


# URL direction to image
urlImage = 'https://raw.githubusercontent.com/Microsoft/ProjectOxford-ClientSDK/master/Face/Windows/Data/identification1.jpg'

# Face detection parameters
params = { 'returnFaceAttributes': 'age,gender', 
           'returnFaceLandmarks': 'true'} 

headers = dict()
headers['Ocp-Apim-Subscription-Key'] = _key
headers['Content-Type'] = 'application/json' 

json = { 'url': urlImage }
data = None

result = processRequest( json, data, headers, params )

if result is not None:
    # Load the original image, fetched from the URL
    arr = np.asarray( bytearray( requests.get( urlImage ).content ), dtype=np.uint8 )
    img = cv2.cvtColor( cv2.imdecode( arr, -1 ), cv2.COLOR_BGR2RGB )

    renderResultOnImage( result, img )

    ig, ax = plt.subplots(figsize=(15, 20))
    ax.imshow( img )


# Load raw image file into memory
pathToFileInDisk = r'D:\tmp\identification1.jpg'
with open( pathToFileInDisk, 'rb' ) as f:
    data = f.read()

# Face detection parameters
params = { 'returnFaceAttributes': 'age,gender', 
           'returnFaceLandmarks': 'true'} 

headers = dict()
headers['Ocp-Apim-Subscription-Key'] = _key
headers['Content-Type'] = 'application/octet-stream'

json = None

result = processRequest( json, data, headers, params )

if result is not None:
    # Load the original image from disk
    data8uint = np.fromstring( data, np.uint8 ) # Convert string to an unsigned int array
    img = cv2.cvtColor( cv2.imdecode( data8uint, cv2.IMREAD_COLOR ), cv2.COLOR_BGR2RGB )

    renderResultOnImage( result, img )

    ig, ax = plt.subplots(figsize=(15, 20))
    ax.imshow( img )

















faceServiceClient = new FaceServiceClient("Your subscription key");

// Create an empty person group
string personGroupId = "myfriends";
await faceServiceClient.CreatePersonGroupAsync(personGroupId, "My Friends");

// Define Anna
CreatePersonResult friend1 = await faceServiceClient.CreatePersonAsync(
    // Id of the person group that the person belonged to
    personGroupId,    
    // Name of the person
    "Anna"            
);

// Define Bill and Clare in the same way