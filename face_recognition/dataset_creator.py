import cv2          #opencv for camera
import numpy as np      #numpy array
import sqlite3         #sqlite is database

faceDetect=cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0); # zero for web camera

# function for sqlite database
def insertOrUpdate(Id,Name,Age):
    conn=sqlite3.connect("database.db ") # connect to database
    cmd = "SELECT * FROM STUDENTS WHERE ID=" + str(Id)
    cursor = conn.execute(cmd)   # cursor has to execute statement
    
    #assume thereis no record in the database
    isRecordExist = 0
    
    for row in cursor:
        isRecordExist = 1
    
    # if we have records in our table
    if (isRecordExist == 1) :
        conn.execute("UPDATE STUDENTS SET Age=? WHERE Id=?", (Age, Id))
        conn.execute("UPDATE STUDENTS SET Name=? WHERE Id=?", (Name, Id))
    # if we have nothing in our table then we insert
    else :
        conn.execute("INSERT INTO STUDENTS(Id,Name,Age) VALUES(?,?,?)",(Id,Name, Age))
        
    conn.commit()
    conn.close()
    
# insert user defined values into the table
id = input('Enter User Id:')
name = input('Enter User Name:')
age = input('Enter User Age:')
# gen=input('Enter User Gender:')


# insertOrUpdate(Id,name,age,gen)
insertOrUpdate(id, name, age)

# detect face in web camera coding

sampleNum = 0  # assume there is no samples in dataset

while(True):
    ret,img = cam.read() # open the camera
    
    # converting the images into gray scale images for accuracy
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5) # scale face
     
    
    for(x,y,w,h) in faces:
        sampleNum = sampleNum + 1  #if face is detected increment
        
        #save the faces in gray and jp
        cv2.imwrite("dataSet/user." + str(id) + "." + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
        
        # create a rectangle to show ditected faces on our camera
        cv2.rectangle(img,(x,y),(x + w, y + h),(0, 255, 0), 2)
        cv2.waitKey(400) # time for showing the faces detected 
        
    cv2.imshow("Face", img) #show faces detected on web cam
    cv2.waitKey(1) 
    
    if(sampleNum > 20): # if dataset is more than 20, break
        break
    
cam.release()
cv2.destroyAllWindows() #quit
