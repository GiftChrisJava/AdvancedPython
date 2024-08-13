import cv2
import numpy as np
import sqlite3

# Load the pre-trained classifier for face detection
faceDetect = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
# Initialize the camera
cam = cv2.VideoCapture(0)

def insertOrUpdate(Id, Name, Age):
    # Connect to the SQLite database
    conn = sqlite3.connect("sqlite.db")
    cursor = conn.execute("SELECT * FROM STUDENTS WHERE ID=?", (Id,))
    
    if cursor.fetchone():
        conn.execute("UPDATE STUDENTS SET Name=?, Age=? WHERE Id=?", (Name, Age, Id))
    else:
        conn.execute("INSERT INTO STUDENTS(Id, Name, Age) VALUES(?,?,?)", (Id, Name, Age))
        
    conn.commit()
    conn.close()

def capture_faces(cam, faceDetect, Id, sample_limit=5):
    sampleNum = 0

    while sampleNum < sample_limit:
        ret, img = cam.read()
        if not ret:
            print("[ERROR] Failed to capture image")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            sampleNum += 1
            cv2.imwrite(f"dataset/user.{Id}.{sampleNum}.jpg", gray[y:y + h, x:x + w])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Face", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("[INFO] Exiting on user request...")
            break

    cam.release()
    cv2.destroyAllWindows()
    print(f"[INFO] Captured {sampleNum} images.")

id = input('Enter User Id:')
name = input('Enter User Name:')
age = input('Enter User Age:')

insertOrUpdate(id, name, age)
capture_faces(cam, faceDetect, id)
