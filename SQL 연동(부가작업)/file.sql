create table images(
	id int primary	key auto_increment,
	forder_name varchar(255),
	file_name varchar(255)
);

-- 위 코드는 테이블 생성하는 코드입니다.

SELECT * FROM users;
-- 이 코드는 현재 users 테이블에 들어가 있는 데이터 리스트를 출력하는 코드입니다.

drop table users;
-- 이 코드는 users 테이블 자체를 삭제하는 코드로 이후 첫번째 create코드로 테이블을 다시 생성해야합니다.

TRUNCATE table users;
-- 이 코드는 users 테이블의 형태는 유지하고 내부 데이터만 삭제하는 코드입니다.
