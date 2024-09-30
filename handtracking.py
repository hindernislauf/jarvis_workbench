# https://github.com/Concept-Bytes/HandTracking.git
# 실행 전 가상환경 활성화 source jarvis/bin/activate

import cv2
import mediapipe as mp


# Initialize Mediapipe Hand solution
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(static_image_mode=False,
                        max_num_hands=2,
                        min_detection_confidence=0.1,
                        min_tracking_confidence=0.1)

mp_drawing = mp.solutions.drawing_utils

# open the camera
cap = cv2.VideoCapture(0)

# error check to make sure the camera is open
if not cap.isOpened():
    print("Error")
    exit()
    

# Main Loop
while True:
    # Capture from by frame from the camera
    success, frame = cap.read()
    if not success:
        break
    
    # Flip the frame horizontally
    # frame = cv2.flip(frame, 1)
    
    # Convert the frame color from BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the RGB frame with MediaPipe Hands
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw Landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            
    # Draw the hand annotations on the frame.
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Drawlandmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
    # Display the resulting frame
    cv2.imshow("Medipipe Hands", frame)
    cv2.waitKey(1)
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()