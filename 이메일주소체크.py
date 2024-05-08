import re  # 정규표현식 모듈을 import합니다.

def check_email(email):
    # 이메일 주소 유효성을 검사하는 정규표현식 패턴
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # 주어진 이메일 주소가 정규표현식 패턴과 일치하는지 확인
    if re.match(pattern, email):
        return True  # 일치하면 유효한 이메일 주소
    else:
        return False  # 일치하지 않으면 유효하지 않은 이메일 주소

def test_email_addresses():
    # 테스트용 이메일 주소 목록
    emails = [
        "user@example.com",
        "john.doe123@gmail.com",
        "alice_123@yahoo.co.kr",
        "info@company.org",
        "first.last@subdomain.example.com",
        "invalid-email",  # 잘못된 형식의 이메일 주소
        "@domain.com",    # 잘못된 형식의 이메일 주소
        "user@.com",      # 잘못된 형식의 이메일 주소
        "user123",        # 잘못된 형식의 이메일 주소
        "user@example"    # 잘못된 형식의 이메일 주소
    ]
    
    # 각 이메일 주소에 대해 유효성 검사 수행
    for email in emails:
        if check_email(email):
            print(f"{email}: 유효한 이메일 주소입니다.")
        else:
            print(f"{email}: 유효하지 않은 이메일 주소입니다.")

# 테스트 실행
test_email_addresses()
