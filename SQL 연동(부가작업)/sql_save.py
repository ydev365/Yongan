import os
import mysql.connector

conn = mysql.connector.connect( #이부분은 mysql서버와 연결하는 부분이라서 mysql설치 및 테이블 생성 시 값을 입력해야합니다
    host="localhost", #호스트 이름
    user="root", #아이디
    password="1234", # 비번
    database="sakila" #테이블 생성한 데이터베이스
)
cursor = conn.cursor()

#사진 데이터 저장된 경로
folder_path = "C:/Users/Desktop 처럼 직접 수정 필요!!!!!!"

files = os.listdir(folder_path)

for user_folder in os.listdir(folder_path):
    user_name = user_folder.split("_")[1]  #폴더 이름의 _부분 이후에서 사용자 이름 추출
    user_folder_path = os.path.join(folder_path, user_folder)
    for file_name in os.listdir(user_folder_path):
        image_path = os.path.join(user_folder_path, file_name)  # 이미지 파일 경로 생성
        # 데이터베이스에 사용자 정보 저장
        insert_query = "INSERT INTO users (name, image_path) VALUES (%s, %s)"
        cursor.execute(insert_query, (user_name, image_path))

#저장
conn.commit()
#종료
cursor.close()
conn.close()
