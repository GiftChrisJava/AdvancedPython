import os  # For handling file operations
import cv2  # For camera operations and image processing
import numpy as np  # For handling arrays
import sqlite3  # For database operations

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

# Initialize the camera (0 indicates the default camera)
cam = cv2.VideoCapture(0)

# Initialize the Local Binary Patterns Histograms Face Recognizer and load the trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recogniser/trainer.yml")

def get_profile(user_id):
    """
    Fetch the profile of a user from the database using their ID.

    Args:
        user_id (int): The ID of the user to fetch from the database.

    Returns:
        tuple or None: The profile data (ID, Name, Age) if found, otherwise None.
    """
    conn = sqlite3.connect("sqlite.db")
    cursor = conn.execute("SELECT * FROM STUDENTS WHERE ID=?", (user_id,))
    profile = cursor.fetchone()  # Fetch the first row, if exists
    conn.close()
    return profile

def draw_profile_info(img, profile, x, y, h):
    """
    Draw the user's profile information on the image.

    Args:
        img (numpy.ndarray): The image frame where the profile information will be drawn.
        profile (tuple): The user's profile containing ID, Name, Age.
        x, y, h (int): Coordinates for positioning the text.
    """
    # Draw the Name and Age below the detected face
    cv2.putText(img, f"Name : {profile[1]}", (x, y + h + 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 127), 2)
    cv2.putText(img, f"Age : {profile[2]}", (x, y + h + 45), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 127), 2)
    # Uncomment and modify the below lines if more information is available in the profile
    # cv2.putText(img, f"Gender : {profile[3]}", (x, y + h + 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 127), 2)

while True:
    # Capture frame-by-frame from the camera
    ret, img = cam.read()
    
    if not ret:
        print("[ERROR] Failed to capture image")
        break

    # Convert the frame to grayscale as face detection works better on grayscale images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Iterate over each detected face
    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Predict the ID and confidence level for the detected face region
        user_id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        # Fetch the user profile from the database using the predicted ID
        profile = get_profile(user_id)

        # If the profile is found, display the user's information
        if profile is not None:
            draw_profile_info(img, profile, x, y, h)

    # Display the resulting frame with the drawn rectangles and profile info
    cv2.imshow("Face", img)

    # Break the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()

# nice, create a python project, that will detect if am sad, happy or just oky by reading my face, add comments to the lines of code you will be generating..
