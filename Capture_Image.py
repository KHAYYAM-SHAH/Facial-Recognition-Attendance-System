import cv2
import os
import csv

def takeImages(Id, name):
    # Ensure TrainingImage directory exists
    if not os.path.exists("TrainingImage"):
        os.makedirs("TrainingImage")

    # Initialize the webcam
    cam = cv2.VideoCapture(0)
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    sampleNum = 0

    print(f"Capturing faces for ID: {Id}, Name: {name}")

    while True:
        ret, img = cam.read()
        if not ret:
            print("Error: Unable to access the camera.")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        for (x, y, w, h) in faces:
            sampleNum += 1
            # Save the captured face in the dataset
            face_path = f"TrainingImage/{name}.{Id}.{sampleNum}.jpg"

            cv2.imwrite(face_path, gray[y:y + h, x:x + w])
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display the video frame
        cv2.imshow("Capturing Faces", img)

        # Stop after 100 images or on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q') or sampleNum >= 100:
            break

    cam.release()
    cv2.destroyAllWindows()

    # Save student details to CSV
    if not os.path.exists("StudentDetails"):
            os.makedirs("StudentDetails")

    csv_file = os.path.join("StudentDetails", "StudentDetails.csv")
    header = ["Id", "Name"]
    row = [Id, name]

        # Write header and row to CSV
    with open(csv_file, 'a+', newline='') as file:
        writer = csv.writer(file)
        if os.stat(csv_file).st_size == 0:  # Check if file is empty
            writer.writerow(header)
        writer.writerow(row)


    print(f"Captured {sampleNum} images for ID: {Id}, Name: {name}")
