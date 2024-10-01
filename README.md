# Jarvis Workbench

이 프로젝트의 목적은 설계, 디자인, 창작 활동 및 DIY 수리를 위한 인공지능 워크벤치를 만들기 위해 시작되었습니다. <br/><br/>
기능의 특정 부분까지는 해외 크리에이터 Concenpt Bytes의 유료 강의를 통해 만들어졌습니다. <br/><br/>
1차적인 목표는 책상 위에서의 작업 활동을 평면적으로 지원하는 Desk Mat Hologram을 만드는 것이고, <br/><br/>
최종적으로는 3차원 공간에서의 작업을 지원하는 3D Hologram Workbench를 구현하는 것이 목표입니다. <br/><br/>
현재까지는 OpenCV와 MediaPipe를 사용하여 실시간으로 손을 추적하고, 추적 내용을 시각적으로 확인할 수 있는 단계까지 구현되었습니다. <br/><br/>
카메라는 유선 웹 카메라, IPWebcam(Android) App을 이용한 스마트폰 카메라를 사용할 수 있습니다. <br/><br/>
스마트폰 네트워크 통신을 이용한 방식은 속도 최적화 방안을 구상 중입니다. <br/><br/>

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
