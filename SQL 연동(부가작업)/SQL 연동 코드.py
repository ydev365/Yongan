import os
import mysql.connector

class TrainFaceData:
    def __init__(self, model_save_path=None, n_neighbors=None, knn_algo='ball_tree', verbose=False):
        self.model_save_path = model_save_path
        self.n_neighbors = n_neighbors
        self.knn_algo = knn_algo
        self.verbose = verbose
        self.knn_clf = None

    def train(self):
        X = []
        y = []

        #이 부분은 mysql서버와 연결하는 부분이라서 mysql설치 및 테이블 생성 시 값을 입력해야합니다
        conn = mysql.connector.connect( 
            host="localhost", #호스트 이름
            user="root", #아이디
            password="1234", # 비번
            database="sakila" #테이블 생성한 데이터베이스
        )
        cursor = conn.cursor()

        # 데이터베이스에서 사용자 정보 불러오기
        cursor.execute("SELECT name, image_path FROM users")
        users = cursor.fetchall()

        for user in users: #user를 users(사용자 정보)에 대해 반복
            name, image_path = user
            image = face_recognition.load_image_file(image_path) #이미지 로드
            face_bounding_boxes = face_recognition.face_locations(image) #face_location, 얼굴 위치 찾음

            if len(face_bounding_boxes) != 1: #위의 face_location으로 찾은 얼굴의 개수가 1개가 아닐시
                if self.verbose: #학습에 부적합할때
                    print(f"이미지 {image_path}는 학습에 적합하지 않음: {'얼굴을 찾지 못함' if len(face_bounding_boxes) < 1 else '여러 얼굴을 찾음'}")
            else: #얼굴이 1개일경우
                face_encoding = face_recognition.face_encodings(image, known_face_locations=face_bounding_boxes)[0] #이미지에서 얼굴 특징 추출
                X.append(face_encoding) #얼굴 특징을 x에 저장
                y.append(name) #이름을 y에 저장

        cursor.close() #커서 close
        conn.close() #SQL 연결 종료

        if self.n_neighbors is None:
            self.n_neighbors = int(round(math.sqrt(len(X))))
            if self.verbose:
                print("자동으로 선택된 n_neighbors:", self.n_neighbors)

        knn_clf = neighbors.KNeighborsClassifier(n_neighbors=self.n_neighbors, algorithm=self.knn_algo, weights='distance')
        knn_clf.fit(X, y)

        if self.model_save_path is not None:
            with open(self.model_save_path, 'wb') as f:
                pickle.dump(knn_clf, f)

        return knn_clf

# KNN 모델 학습
train_data = TrainFaceData(model_save_path=None, n_neighbors=None, knn_algo='ball_tree', verbose=True)
knn_clf = train_data.train()
