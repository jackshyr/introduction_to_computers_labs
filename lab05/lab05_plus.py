dic0 = {}
for i in range(0,4):  
    l = []
    a = input()#讀入key
    for j in range(0,5):
        l.append(input())#讀入value
    dic0.update({a:l})
for i in dic0:#輸出字典
    print(i)
    print(dic0[i])
