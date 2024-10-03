import cv2
import mediapipe as mp
import pyautogui as pag
import numpy as np

def main():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False,
                           max_num_hands=2,
                           min_detection_confidence=0.1,
                           min_tracking_confidence=0.1)
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: 카메라를 열 수 없습니다. 연결 상태를 확인하세요.")
        exit()

    screen_width, screen_height = pag.size()
    mouseDown = False

    while True:
        success, frame = cap.read()
        if not success:
            break
        
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        
        frame_height, frame_width, _ = frame.shape
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                
                midpoint_x = (index_finger_tip.x + thumb_tip.x) / 2
                midpoint_y = (index_finger_tip.y + thumb_tip.y) / 2
                
                distance = np.sqrt((index_finger_tip.x - thumb_tip.x)**2 + (index_finger_tip.y - thumb_tip.y)**2)
                
                if distance < 0.1 and not mouseDown:
                    pag.mouseDown()
                    mouseDown = True
                
                if distance > 0.3 and mouseDown:
                    pag.mouseUp()
                    mouseDown = False
                    
                circle_color = (0, 255, 0) if mouseDown else (0, 0, 255)
                cv2.circle(frame, (int(midpoint_x * frame_width), int(midpoint_y * frame_height)), 10, circle_color, -1 if mouseDown else 1)
                
                x_mapped = np.interp(midpoint_x, (0, 1), (0, screen_width))
                y_mapped = np.interp(midpoint_y, (0, 1), (0, screen_height))
                
                pag.moveTo(x_mapped, y_mapped, duration=0.1)
                
        cv2.imshow("Medipipe Hands", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()