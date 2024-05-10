from openpyxl import Workbook
import random

# 제품 데이터 생성
products = []
for i in range(100):
    product_id = i + 1
    product_name = f"제품{product_id}"
    quantity = random.randint(1, 100)
    price = round(random.uniform(10, 1000), 2)
    products.append((product_id, product_name, quantity, price))

# 엑셀 파일 생성과 데이터 입력
wb = Workbook()
ws = wb.active
ws.title = "제품목록"

# 헤더 추가
ws.append(["제품ID", "제품명", "수량", "가격"])

# 제품 데이터 추가
for product in products:
    ws.append(product)

# 엑셀 파일 저장
file_path = r'c:\work2\products.xlsx'
wb.save(file_path)

print(f"제품 데이터가 {file_path} 경로에 저장되었습니다.")
