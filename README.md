# iot--face-recognition
face recognition based iot authentication
# iot--face-recognition
banana pi based iot project for home automation with face recognition

intro


This is a face authenticated home automations system, data & trainner.py helps to make data set and trainner .yml file which is a numpy
array saved to the folder train
The final.py recogonises the known and un know face and redirects to the respective url.
 
 
 This can be connected to an ip camera as it is or connected to a smartphone using the CloudCam app which comes with a jar file inbuild i have
 integrated it to the python script to run on itself and call the regonisition program by itself, using jarr.py
 
 this project is built using open cv 3.1 lbphfrecogonizer for face detection
 
 run the script:
 
 i  testested this on Armbian linux running on banana pi as its default bananian failed to compile openCV with ffmpeg. 
 face can be trained using smartphone camera on a desktop or laptop (since arm boards are slow) using data&train.py, one may use ipwebcam on android
 or CloudCamapp i used Cloud cam app since it can run on mobile network aswellas one could access this system using global ip of ur pi board
   
if you are using the Cloudcam app you start the jarr.py using the local ip of the system in which the face recognition program is runs
and note that is is configured properly on your app as well(all those instructions are well documented in the app itself).
this script would call the final.py as soon as the phone is connected to the pi. the final.py will launch the web page on the same ip and
port 80 there are 2 webpages if the system identifies the trained face then it would launch automate.py which is an flask webpage else to
fail.py

Jarr.py is set with timer to kill the entire process in 7 minutes therefore you can access this web page only for 5 minutes then you have 
login again.
 
 therefore once the system is trained you just have to run jarr.py on the home server and you may connect you phone from around the world 
 and automate the home.
 
 the face recognition examples are available in the the following links

http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html

https://www.superdatascience.com/opencv-face-detection/

https://thecodacus.com
