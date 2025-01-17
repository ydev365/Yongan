import face_recognition
import cv2
import numpy as np
import os


known_face_encodings = []
known_face_names = []

# 본인 사진 데이터 위치에 맞게 경로 수정 해야함 !!!!!!, 
base_dir = "C:/Users/desktop 처럼 직접 수정하세요"

# 각 하위폴더 이름
names = ["yongan_YYS", "yongan_JHS", "yongan_CYW", "yongan_KMJ", "yongan_PJS"]
display_names = ["Yoon_Yong_Sun", "Jung_Hee_Sang", "Choi_Ye_Won", "Kang_Min_Ju", "Park_Jun_Soo"]


for i, name in enumerate(names):
    person_dir = os.path.join(base_dir, name)
    for img_name in os.listdir(person_dir):
        img_path = os.path.join(person_dir, img_name)
        img = face_recognition.load_image_file(img_path)
        encodings = face_recognition.face_encodings(img)
        if encodings:  
            known_face_encodings.append(encodings[0])
            known_face_names.append(display_names[i])


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = np.ascontiguousarray[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
