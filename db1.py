# db1.py
import sqlite3

#전역함수:임시로 메모리에 작업
#연결객체(인스턴스)
con = sqlite3.connect(":memory:")

#실제 구문 실행 커서 객체
cur = con.cursor();

#테이블 구조(데이터 저장소)
cur.execute("CREATE TABLE PhoneBook (Name text, PhoneNum text);")

#입력
cur.execute("insert into PhoneBook values ('전우치', '010-222-0001');")

#입력 파라미터 처리
name = "홍길동"
phoneNumber = "010-123-4567"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))

#한번에 2개를 입력(다중 행 입력)
dataList = (("이순신", "010-111-1111"), ("박문수", "010-222-2222"))
cur.executemany("insert into PhoneBook values (?, ?)", dataList)

#검색
cur.execute("select * from PhoneBook;")

for row in cur:
    print(row[0], row[1])
