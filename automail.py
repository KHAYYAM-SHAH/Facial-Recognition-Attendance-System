import cv2
import face_recognition
import numpy as np
import datetime
import os
from openpyxl import Workbook

# Load the attendance workbook
wb = Workbook()
ws = wb.active

# Set the header row
ws['A1'] = 'Name'
ws['B1'] = 'ID'
ws['C1'] = 'Date'
ws['D1'] = 'Time'
ws['E1'] = 'Present'

# Initialize the row counter
row = 2

# Load the known faces and IDs
known_faces = []
known_ids = []

# Load the face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        face = gray[y:y+h, x:x+w]
        face_encoding = face_recognition.face_encodings(face)[0]

        # Check if the face is known
        for i, known_face in enumerate(known_faces):
            match = face_recognition.compare_faces([known_face], face_encoding)
            if match[0]:
                name = known_ids[i]
                id = i
                break
        else:
            name = 'Unknown'
            id = None

        # Add the attendance data to the spreadsheet
        ws.cell(row=row, column=1).value = name
        ws.cell(row=row, column=2).value = id
        ws.cell(row=row, column=3).value = datetime.date.today().strftime('%Y-%m-%d')
        ws.cell(row=row, column=4).value = datetime.datetime.now().strftime('%H:%M:%S')
        ws.cell(row=row, column=5).value = 'Present'
        row += 1

        # Save the workbook
        wb.save('DailyAttendance/attendance.xlsx')

    cv2.imshow('Attendance System', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()