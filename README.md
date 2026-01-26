# Hand-Motion-Based-System-Controls-Manager

We are a team of two members and worked on our final year project. This project allows controlling system functions such as mouse functionalities (cursor movement, text selection, cursor locking), volume, brightness, zoom, and tab controls using hand gestures. OpenCV and MediaPipe modules are used to interpret gestures. The system employs a webcam to capture images and videos, enabling control over functions such as adjusting volume, brightness, mouse movements, clicks, scrolling, tab switching, minimization, closing, copying/pasting text, and zooming in/out for windows or PDF files. To distinguish gestures, we use a 5-bit binary digit list-based approach for finger up-down detection. Through real-time gesture recognition, users can manipulate a computer with hand gestures.

Modules and Features

Existing Features

Volume controller: controlling volume using pinch gesture

Brightness controller: controlling brightness using pinch gesture

Mouse: cursor movement, right click, left click, scroll-up & scroll-down

Proposed Features

Tabs controller: tab minimization, tab swapping, tab closing

Zoom controller: window zoom in/out, document or PDF zoom in/out

Copy & paste: copying and pasting images or text

Modifications to Existing Features

Volume controller: gesture detection based on hand bounding box area, set volume using pinky finger

Brightness controller: gesture detection based on hand bounding box area

Mouse: cursor locking, text selection

Working of Implementation Block Diagram for our model:
“Gestures are represented as a 5-finger binary pattern (1 = up, 0 = down) combined with hand side (‘Left’ or ‘Right’) to detect commands.”


![gesture pipeline](https://github.com/user-attachments/assets/84c97f37-96c6-4ed8-9c16-6031f51e8ca6)



Understanding of above block diagram involves mapping of specified 5-bit binary numbers with respect to each hand gesture i.e. 


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/d1d90478-0006-4efc-b901-23172a7e778e)


Implementations:
A.	Tabs Controller:
A gesture sequence i.e. {Left, [0,1,1,1,1]} -> {Left, [0,1,0,0,1]} -> {Left, [0,1,1,1,1]} will switch to the next tab.


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/8f65dbf3-ff10-4255-98be-488543711fba)


A gesture sequence i.e. {Left, [0,1,1,1,0]} -> {Left, [0,1,0,0,1]} -> {Left, [0,1,1,1,1]}  will close the current tab.


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/e47122f7-3ae8-4d63-8b8f-a9a38ad0056e)


A gesture sequence i.e. {Left, [0,1,1,1,1]} -> {Left, [0,1,0,0,1]} -> {Left, [0,1,1,1,1]}  will minimize all the current tabs.


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/ea6bb245-ba56-45fe-bcbd-a46516bb6091)


B.	Zoom in-out Controller:
Controlling window or PDF file zoom in/out using hand gestures.
Mapped gesture for zoom in-out for Window is {Left, [1,0,0,0,1]},


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/6220735a-0a21-48cf-9829-2d1dffd4a421)


while for pdf or document file zoom in-out is {Left, [0,1,0,0,1]}.


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/29f88873-73e1-4eee-ad48-9c99f617d6df)


Based on area of Bounding box created around hand gesture. This works as :
If area(current frame bounding box) < area(previous frame bounding box) 
      then Perform zoom out.
Elif area(current frame bounding box) > area(previous frame bounding box) 
      then Perform zoom in.

C.	Virtual mouse:  
Gesture encoding for the cursor movement function i.e. {Right, [1,1,1,0,0]}, 
also for the text selection i.e. {Right, [1,1,0,0,1]},
Finally for , click& Double click functions i.e. {Right, [0,1,0,0,0]} or {Right, [0,1,1,0,0]} & for cursor locking function i.e. {Right, [1,1,0,0,0]}:


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/befa1933-ceda-49de-9775-b6c9ddb00bff)


D.	Copy{Right,[0,1,0,0,0]} & Paste{Right,[0,1,1,0,0]} Controller:


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/d0ded4bd-43be-4adc-8fec-9d01612c7710)


E.	Volume controller{Right,[1,1,1,1,1]}:


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/4e6526c7-3621-44d0-908a-43e122ace3b8)


F.	Brightness controller{Left,[1,1,0,0,1]}:


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/241e4d43-cfe2-4c1d-aba1-44dd298f93ea)


G.  Scroll-Up{Left,[0,1,1,0,0]}&Scroll- Down{Left,[0,1,0,0,0]}:


![image](https://github.com/555Chaithanya/Hand-Motion-Based-System-Controls-Manager/assets/81861417/0c6fc2e4-d07e-440c-920a-255848afca65)


Future Scope: Integrating Natural Language Processing (NLP) via the Whisper module to create a multimodal command chain (Gesture Audio recording -> Another next gesture speech to Text and copied to  Clipboard. By paste gesture we have already we can paste text in editors without typing).


You can see Demo of Implementation Below:
_____________________________________________________________________________________
https://drive.google.com/drive/folders/1EugLwEZTLKwi2D_IJF12hW_S9HHY05wF?usp=sharing
_____________________________________________________________________________________

