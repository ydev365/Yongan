import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="sakila"
)
cursor = conn.cursor()

# 데이터베이스에서 사용자 정보 불러오기
cursor.execute("SELECT name, image_path FROM users")
users = cursor.fetchall()

# 사용자 정보를 담을 리스트 초기화
known_face_encodings = []
known_face_names = []

# 데이터베이스에서 불러온 사용자 정보를 로드합니다.
for user in users:
    name, image_path = user
    # 이미지 파일인지 확인합니다.
    # 이 부분은 예원님 데이터 권한문제로 추가한 코드로 이 코드때문에 현재 예원님 데이터는 얼굴인식 코드에 전달되지 않습니다.
    if not os.path.isfile(image_path):
        continue
    img = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(img)
    if encodings:  
        known_face_encodings.append(encodings[0])
        known_face_names.append(name)
