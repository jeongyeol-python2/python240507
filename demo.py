# demo.py
strA="파이썬은 강력해"
print( strA )
print( len(strA ))
print ( strA[0:3] )
colors=["red","green","bule"]
print(colors)
colors.insert(1, "white")
print(colors)

t=(1,2,3)
type(t)

def calc(a,b):
    return a+b, a*b
x,y=calc(5,4)
print(x,y)
args=(3,4)
print(calc(*args))

for i in range(5):
        print(i)

# Demo List Tuple

print("--List---")
lst = [1,2,3]
print(len(lst))
lst.append(4)
print(lst)
lst.remove(2)
print(lst)

print("--Tuple---")
tp=(10, 20,30)
print(len(tp))

print("---Set-----")
a={1,2,3}
b={3,4,5}
print( a.union(b))
print( a.intersection(b))
print( a.difference(b))

print("----Tuple use----")
#함수 정의 문법(이렵 파라미터 a,b)
def calc(a,b):
    return a+b, a*b

#호출
result = calc(3,4)
print(result)

print("id: %s, name: %s" %("kim", "김유신"))

args=(5,6)
print(calc(*args))

print("----형식 변환----")
a=list((10,20,30))
a.append(40)
print(a)

print("----dict-----")
color["cherry"]="red"
color