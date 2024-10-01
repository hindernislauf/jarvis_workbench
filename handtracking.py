# https://github.com/Concept-Bytes/HandTracking.git
# 실행 전 가상환경 활성화 source jarvis/bin/activate

import cv2
import mediapipe as mp


# Mediapipe Hand solution 초기화
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(static_image_mode=False,
                        max_num_hands=2,
                        min_detection_confidence=0.1,
                        min_tracking_confidence=0.1)

mp_drawing = mp.solutions.drawing_utils

# open the camera
cap = cv2.VideoCapture(0)

# 카메라 상태 체크
if not cap.isOpened():
    print("Error: 카메라를 열 수 없습니다. 연결 상태를 확인하세요.")
    exit()
    

# 메인 루프
while True:
    # Capture from by frame from the camera
    success, frame = cap.read()
    if not success:
        break
    
    # 카메라 수평 반전. 내장 카메라 사용 시 주석 해제
    # frame = cv2.flip(frame, 1)
    
    # 프레임 컬러를 BGR에서 RGB로 변경
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # RGB 프레임을 MediaPipe Hands로 처리
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw Landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            
    # 프레임에 hand annotations 표시(손 위치, 모양 등을 시각적으로 표시)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Drawlandmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
    # 프레임 결과값 디스플레이
    cv2.imshow("Medipipe Hands", frame)
    cv2.waitKey(1)
    
# 주요 로직이 모두 실행되면, 카메라 입력 장치의 사용을 종료.
cap.release()
cv2.destroyAllWindows()