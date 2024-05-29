import subprocess
import sys

# Function to install a package using pip
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install OpenCV package
install("opencv-python")

import cv2

# Load the pre-trained face classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces in an image
def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces

# Function to assign famous names to detected faces
def assign_names_to_faces(faces):
    # List of famous names
    famous_names = ["ayoub", "Leonardo da Vinci", "Marie Curie", "Nelson Mandela", "Oprah Winfrey", "Steve Jobs", "Ada Lovelace", "William Shakespeare"]

    # Assign famous names to detected faces
    assigned_names = []
    for i in range(len(faces)):
        if i < len(famous_names):
            assigned_names.append(famous_names[i])
        else:
            assigned_names.append("Unknown")
    return assigned_names

# Main function
def main():
    # Video capture from webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        # Detect faces in the captured frame
        faces = detect_faces(frame)

        # Assign famous names to detected faces
        assigned_names = assign_names_to_faces(faces)

        # Draw rectangles around detected faces and display assigned names
        for (x, y, w, h), name in zip(faces, assigned_names):
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Display the assigned name above the rectangle
            cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

        # Display the frame with detected faces and names
        cv2.imshow('Face Detection', frame)

        # Quit if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release webcam capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
