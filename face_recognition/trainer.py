import os  # For reading and writing files
import cv2  # For camera operations and image processing
import numpy as np  # For handling arrays
from PIL import Image  # For image file read and write operations

# Initialize the Local Binary Patterns Histograms Face Recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Path to the dataset containing face images
path = "dataset"

def get_images_with_id(path):
    """
    This function retrieves the image files from the specified directory, 
    converts them into grayscale, extracts the user ID from the file name, 
    and returns arrays of IDs and the corresponding face images.

    Args:
    path (str): The directory path containing the face images.

    Returns:
    tuple: A tuple containing an array of IDs and a list of face images.
    """
    # Get the full path to each image in the dataset folder
    images_path = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []  # List to store face images
    ids = []  # List to store corresponding user IDs
    
    for single_image in images_path:
        # Open the image and convert it to grayscale
        faceImg = Image.open(single_image).convert('L')
        faceNp = np.array(faceImg, np.uint8)  # Convert the image to a numpy array (8-bit)
        
        # Extract the user ID from the image filename
        id = int(os.path.split(single_image)[-1].split(".")[1])
        print(id)
        
        # Append the face image and the corresponding ID to their respective lists
        faces.append(faceNp)
        ids.append(id)
        
        # Display the image during training (optional, can be removed)
        cv2.imshow("Training", faceNp)
        cv2.waitKey(100)  # Wait for 100 ms between showing images
        
    # Convert the lists to numpy arrays for compatibility with the recognizer
    return np.array(ids), faces

# Example usage
ids, faces = get_images_with_id(path)
recognizer.train(faces, ids)
recognizer.save("recogniser/trainer.yml")  # Save the trained model to a file
cv2.destroyAllWindows()  # Close all windows after training