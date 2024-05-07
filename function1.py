# function1.py

#함수 이름 해석 규칙(L-local, G-grobal, B-built in - 내장함수)
#전역변수가 있는 경우
x=1
def func(a):
    return a+x

#호출
print(func(1))

#지역변수가 있는 경우
def func2(a):
    x=5
    return a+x

#호출
print(func2(1))

#함수의 기본값
def times(a=10, b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드 인자방식 (상세 기술)
def connectURI(server, port):
    strURL = "https://" + server + ":" + port
    return strURL

#호출
print(connectURI("multi.com", "80"))
print(connectURI(port="80", server="naver.com"))

#가변인자 처리
def union(*ar):
    #지역변수 저장(list)
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HMM","EGG"))
print(union("HMM","EGG","SPAM"))

#람다 함수
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))

#2024.05.07 end

#불변형식
a = 1.2
print("a id:", id(a) )
a = 2.3 
print("a id:", id(a) )

#가변형식
lst = [1,2,3]
print("lst id:", id(lst) )
lst.append(4)
print("lst id:", id(lst) )
print(lst)

#가변형식
def change(x):
    #지역변수로 깊은 복사
    x1 = x[:]
    x1[0] = "H"
    print("change함수내부:", x1)

#함수 호출
wordlist = ["J","A","M"]
change(wordlist)
print("함수 호출후:", wordlist)

#불변형식인데 읽기/쓰기를 하는 경우
g = 1 
def testScope(a):
    #전역변수를 맵핑
    #global g 
    g = 2 
    return g + a 

#함수 호출
print( testScope(1) ) 
print("전역변수 g:", g)

#디버깅 
#교집합 리턴하는 함수 
def intersect(prelist, postlist):
    retList = []
    for x in prelist:
        if x in postlist and x not in retList:
            retList.append(x)
    return retList 


#호출
print( intersect("HAM", "SPAM") )

