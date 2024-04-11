# Hand-Motion-Based-System-Controls-Manager
We are a team of two members, worked on our final year project.This Project offers a more intuitive approach to managing a maximum number of system controls such as mouse functionalities like cursor movement, text selection with the cursor, cursor locking, volume and brightness control with set feature, and area-based detection, Zoom controls &amp; Tab Controls virtually using transition in hand Gestures.
In this project, we have developed an Hand Motion Based System Controls Manager, utilizing hand gestures as input for system manipulation virtually. OpenCV and Media-Pipe modules form the basis of this implementation to interpret gestures. The system employs a webcam to record or capture images and videos, enabling control over various functions such as adjusting volume, brightness, mouse movements, clicks, scrolling, cursor locking for comfortable clicks, tab controls including tab switching, minimization, closing, as well as copying and pasting text through gestures, and zooming in and out for windows or PDF files. 
To distinguish between the many gestures, we have introduced a 5-bit binary number-based approach, facilitating the implementation of multiple gestures simultaneously. Through real-time gesture recognition, specific users can manipulate a computer using hand gestures in front of a camera linked to the system. This approach enables system control via hand gestures, reducing reliance on keyboard and mouse controls to some extent.
Also there exist a lot of projects with individual features i.e.
Modules	                                    Existing  features
Volume controller	                          Controlling volume using Pinch gesture
Brightness Controller	                      Controlling brightness using Pinch gesture
Mouse	                                      Curser Movement, Right click, Left Click, Scroll-up & Scroll-down

The newly proposed features include:
Modules	                                    Proposed features
Tabs controller	                            Tab Minimization, Tabs Swapping, Tab closing
Zoom Controller	                            Window Zoom in-Zoom out, Document or Pdf Zoom in-Zoom out.
Copy & Paste	                              Copying of images or text, Pasting of images or text.

The modifications added for existing features are:
Modules	                                    Proposed features
Volume controller	                          Addition of gesture detection based on hand’s bounding box area, Set volume based on pinky finger
Brightness Controller	                      Addition of gesture detection based on hand’s bounding box area, Set brightness based on [11111] gesture
Mouse	                                      Locking Curser , Text Selection.

Working of Implementation Block Diagram for our model:


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/9b3d7084-cde6-42be-8d9d-335170848f24)


Understanding of above block diagram involves mapping of specified 5-bit binary numbers with respect to each hand gesture i.e. 


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/d1d90478-0006-4efc-b901-23172a7e778e)


Implementations:
A.	Tabs Controller:
The approach to implement controlling of  tabs using hand gestures:
A transition of encoding i.e. {Left, [01111]} -> {Left, [01001]} -> {Left, [01111]} will switch to the next tab.


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/8f65dbf3-ff10-4255-98be-488543711fba)


A transition of encoding i.e. {Left, [01110]} -> {Left, [01001]} -> {Left, [01111]}  will close the current tab.


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/e47122f7-3ae8-4d63-8b8f-a9a38ad0056e)


A transition of encoding i.e. {Left, [01111]} -> {Left, [01001]} -> {Left, [01111]}  will minimize all the current tabs.


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/ea6bb245-ba56-45fe-bcbd-a46516bb6091)


B.	Zoom in-out Controller:
Controlling window or PDF file zoom in/out using hand gestures can be achieved using computer vision libraries like OpenCV and gesture recognition techniques.
Mapped encoding for zoom in-out for Window is {Left, [10001]},


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/6220735a-0a21-48cf-9829-2d1dffd4a421)


while for pdf or document file zoom in-out is {Left, [01001]}.


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/29f88873-73e1-4eee-ad48-9c99f617d6df)


Based on area of Bounding box created around hand gesture. The algorithm works as :
If area(current frame bounding box) < area(previous frame bounding box) 
      then Perform zoom out.
Elif area(current frame bounding box) > area(previous frame bounding box) 
      then Perform zoom in.

C.	Virtual mouse:
The proposed virtual mouse module is based on the images that have been captured by the laptop’s or PC’s webcam. The virtual mouse system utilizes an algorithm that translates fingertip coordinates from the webcam screen to the entire computer window screen, enabling mouse control.  
Gesture encoding for the cursor movement function i.e. {Right, [11100]}, 
also for the text selection i.e. {Right, [11001]},
Finally for , click& Double click functions i.e. {Right, [01000]} or {Right, [01100]} & for cursor locking function i.e. {Right, [11000]}:


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/befa1933-ceda-49de-9775-b6c9ddb00bff)


D.	Copy & Paste Controller:
Gesture encoding for the cursor movement function i.e. {Right, [11100]}, while for cursor locking function i.e. {Right, [11000]}, also for the text selection i.e. {Right, [11001]}, finally for , click& Double click functions i.e. {Right, [01000]} or {Right, [01100]}.


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/d0ded4bd-43be-4adc-8fec-9d01612c7710)


E.	Volume controller:


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/4e6526c7-3621-44d0-908a-43e122ace3b8)


F.	Brightness controller:


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/241e4d43-cfe2-4c1d-aba1-44dd298f93ea)


G.  Scroll-Up{Left,[01100]}&Scroll- Down{Left,[01000]}:


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/0c6fc2e4-d07e-440c-920a-255848afca65)


You can see Demo of Implementation Below:
_____________________________________________________________________________________
https://drive.google.com/drive/folders/1EugLwEZTLKwi2D_IJF12hW_S9HHY05wF?usp=sharing
_____________________________________________________________________________________

