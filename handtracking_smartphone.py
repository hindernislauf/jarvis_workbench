import cv2
import mediapipe as mp
import numpy as np
import requests
from threading import Thread
from queue import Queue
import time

def capture_frames(url, frame_queue):
    while True:
        img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        frame = cv2.imdecode(img_arr, -1)
        if frame is not None:
            if frame_queue.qsize() < 2:
                frame_queue.put(frame)
            else:
                try:
                    frame_queue.get_nowait()
                except Queue.Empty:
                    pass
                frame_queue.put(frame)
        time.sleep(0.01)

def main(ip_address="10.186.26.22", port="8080"):
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False,
                           max_num_hands=2,
                           min_detection_confidence=0.5,
                           min_tracking_confidence=0.5)
    mp_drawing = mp.solutions.drawing_utils

    url = f"http://{ip_address}:{port}/shot.jpg"
    frame_queue = Queue(maxsize=2)
    
    capture_thread = Thread(target=capture_frames, args=(url, frame_queue))
    capture_thread.daemon = True
    capture_thread.start()

    frame_count = 0
    while True:
        if not frame_queue.empty():
            frame = frame_queue.get()
            frame_count += 1

            if frame_count % 2 == 0:
                continue

            frame = cv2.resize(frame, (640, 480))
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_frame)
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            cv2.imshow("Handtracking Smartphone", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()