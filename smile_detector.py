import cv2
import sys


# face dectection
face_detector =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector =cv2.CascadeClassifier('haarcascade_smile.xml')

# Grab WebCam Feed
webcam = cv2.VideoCapture(0)

# Show the current time
while True:
    # Read current frame from webcam video stream
    successful_frame_read, frame = webcam.read()

    # If there's an error
    if not successful_frame_read:
        break

    # Change to gray scale
    frame_grayscale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Detect face first
    faces = face_detector.detectMultiScale(frame_grayscale)

    # Run smile dectection with in each of those faces
    for (x, y, w, h) in faces:

        # Draw a rectangle around the face
        cv2.rectangle(frame,(x,y),(x+w, y+w), (100, 200, 50),4)

        # Get the sub frame (using numpy N-dimesntional array slicing )
        the_face =frame[ y:y+h, x:x+w]

        # Change to grayscale
        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

        smiles = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=20)

        # Find all smiles in the face

        for (x_, y_, w_, h_) in smiles:

            # Draw a rectangle around the face
             cv2.rectangle(the_face,(x_, y_),(x_+w_, y_+w_), (50, 50, 200),4)
        if len(smiles)>0:
            cv2.putText(frame,'smiling',(x, y+h+40), fontScale=3,fontFace=cv2.FONT_HERSHEY_PLAIN,color=(255,255,255))


    # Show the current Frame
    cv2.imshow('Why so serious?', frame)

    # Display
    cv2.waitKey(1)

#Clean up
webcam.release()
cv2.destroyAllWindows()
