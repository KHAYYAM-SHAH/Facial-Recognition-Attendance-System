from flask import Flask, render_template, request
import check_camera
import Capture_Image
import Train_Image
import Recognize

app = Flask(__name__)

@app.route("/")
def home():
    # Render the main HTML interface
    return render_template("mainindex.html")

@app.route("/check_camera.py", methods=["GET"])
def check_camera_route():
    check_camera.camer()
    return "Camera checked successfully!"

@app.route("/Capture_Image.py", methods=["GET", "POST"])
def capture_faces_route():
    if request.method == "POST":
        # Get ID and Name from the form
        user_id = request.form["id"]
        user_name = request.form["name"]

        # Call the Capture_Image function with the provided ID and Name
        Capture_Image.takeImages(user_id, user_name)
        return f"Faces captured successfully for ID: {user_id}, Name: {user_name}"
    return render_template("/Capture_Image.py")

@app.route("/Train_Image.py", methods=["GET"])
def train_images_route():
    Train_Image.TrainImages()
    return "Images trained successfully!"

@app.route("/Recognize.py", methods=["GET"])
def recognize_faces_route():
    Recognize.recognize_attendence()
    return "Faces recognized and attendance marked!"

if __name__ == "__main__":
    app.run(debug=True)
