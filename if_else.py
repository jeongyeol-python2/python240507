#분기 반복 구문
score = 99 #int(input("점수를 입력:"))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
else:
    grace = "F"
    
print("Grade is " + grade)

value = 5
while value > 0:
    print(value)
    value -= 1

lst = [100, "apple", 3.14]
for item in lst:
    print(item)

fruits = {"apple": 100, "kiwi":200}
for k,v in fruits.items():
    print(k, v)

print("----range() 함수----")
print(list(range(2000,2025)))
print(list(range(1,32)))