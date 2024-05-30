#파란 박스 생성

import cv2

# 얼굴 감지기를 초기화합니다.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 연결된 카메라의 인덱스를 지정합니다.
# 일반적으로 0은 내장 웹캠을, 1은 외부 카메라를 가리킵니다.
cap = cv2.VideoCapture(0)

while True:
    # 카메라에서 프레임을 읽어옵니다.
    ret, frame = cap.read()

    # 프레임을 회색으로 변환합니다. (얼굴 감지기는 회색 이미지를 요구합니다.)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 감지기를 사용하여 얼굴을 감지합니다.
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 감지된 얼굴 주변에 사각형을 그립니다.
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # 화면에 프레임을 표시합니다.
    cv2.imshow('Face Detection', frame)

    # 'q' 키를 누르면 반복문을 종료합니다.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 작업이 끝났으므로 카메라를 해제합니다.
cap.release()

# 화면에 표시된 창을 모두 닫습니다.
cv2.destroyAllWindows()
