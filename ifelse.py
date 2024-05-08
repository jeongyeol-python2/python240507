#ifelse.py

print("---Range() 함수---")
print(list(range(2000, 2025)))
print(list(range(1, 32)))

print("---List 함수---")
lst = list(range(1,11))
print(lst)
print([i**2 for i in lst if i>5])

d={100:"apple",200:"kiwi"}
print([v.upper() for v in d.values()])

print("---필터링 함수 적용 전---")
lst = [10, 25, 30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

#함수 정의
def getBiggerThan20(i):
    return i>20

print("---필터링 함수 적용 후---")
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

print("---필터링 함수 - 람다 적용 후---")
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)