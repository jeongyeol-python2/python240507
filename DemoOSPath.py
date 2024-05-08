# DemoOSPath.py
import os
import os.path
import random

print(random.random())
print(random.random())
#중복 가능
print([random.randrange(20) for i in range(10)]) 
print([random.randrange(20) for i in range(10)])
print("---샘플링---")
#중복 제외
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))

print(random.sample(range(1,46),6))

fileName = r"c:\python39\python.exe"
print(os.path.abspath("python.exe"))
print(os.path.basename(fileName))

if os.path.exists(fileName):
    print("파일크기: ", os.path.getsize(fileName))
else:
    print("파일 없음")

import glob

print(glob.glob("c:\\work2\\*.py"))