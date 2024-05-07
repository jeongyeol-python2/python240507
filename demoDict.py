#demoDict.py

colors={"apple":"red","banana":"yellow"}
print(colors)
print(type(colors))
print(len(colors))

#append
colors["kiwi"]="green"
print(colors)

#delete
del colors["apple"]
print(colors)

for item in colors.items():
    print(item)

for k,v in colors.items():
    print(k,v)

