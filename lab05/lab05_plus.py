dic0 = {}
for i in range(0,4):  
    l = []
    a = input()
    for j in range(0,5):
        l.append(input())
    dic0.update({a:l})
for i in dic0:
    print(i)
    print(dic0[i])
