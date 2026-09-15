Face Recognition Attendance System

Recognizes faces and marks attendance automatically.

Features

Check camera
Capture faces
Train faces
Recognize faces and log attendance
Auto email (experimental, not fully wired in)

How it works

Register — enter student ID + name, capture face images through the webcam
Train — the system learns those faces and builds a recognition model
Recognize — live camera checks each face against the trained model
Attendance — if the match confidence passes the threshold, the student is marked present and logged automatically

Tech used

Python
OpenCV (Haar Cascade for face detection, LBPH for face recognition)
Pandas (attendance logging/export)
Pillow, NumPy (image processing)
CSV / Excel for storage

Known limitation

Auto-email attachment still needs some work to do like implementation and is not fully automated yet.

Image for Reference:
 <img width="1200" height="700" alt="face_recognition_frontend" src="https://github.com/user-attachments/assets/9c9b263f-1af7-4bbe-933d-131901a184c5" />
