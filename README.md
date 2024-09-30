# jarvis_workbench

이 프로젝트는 OpenCV와 MediaPipe를 사용하여 실시간으로 손을 추적하고 시각화합니다.

## 설치 요구사항

이 프로젝트를 실행하기 위해서는 Python 3.7 이상이 필요합니다.

1. 가상 환경 생성 및 활성화:
python3 -m venv jarvis
source jarvis/bin/activate

2. 필요한 패키지 설치:
pip install -r requirements.txt

## 실행 방법

1. 가상 환경 활성화:
source jarvis/bin/activate

2. 스크립트 실행:
python handtracking.py

## 주의사항

- 외부 웹캠을 사용하는 경우, `cv2.VideoCapture(0)` 의 인덱스를 적절히 조정해야 할 수 있습니다.
- 카메라 영상이 반전되어 보이는 경우, 코드 내의 `cv2.flip()` 함수 사용을 조정하세요.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.