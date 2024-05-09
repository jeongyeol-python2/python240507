# db2.py
import sqlite3

#전역함수:임시로 메모리에 작업
#연결객체(인스턴스) : 메모리, 테스트 용도
#con = sqlite3.connect(":memory:")
#영구 테이블
con = sqlite3.connect("c:\\work2\\simple.db")

#실제 구문 실행 커서 객체
cur = con.cursor()

#테이블 구조(데이터 저장소) : 테이블이 없을 경우에 생성
cur.execute("CREATE TABLE if not exists PhoneBook (Name text, PhoneNum text);")

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

print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())

#작업 완료
cur.close()