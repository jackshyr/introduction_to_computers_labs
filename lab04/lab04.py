l = []
ave = []
for i in range(0,3):
    sum = 0
    if i==0:
        A="A"
    elif i==1:
        A="B"
    else:
        A="C"
    print("開始輸入"+A+"學生的成績,請依照 國文,英文,數學,自然,社會 的順序輸入:")#要求使用者輸入ABC三人的成績
    row =[]
    j = 0
    while j<5:
        row.append(int(input()))#讀入5科成績
        j = j+1
    l.append(row)#建立二維陣列
    for k in range(0,5):
        sum = sum+ row[k]
    sum = sum/5#計算平均
    ave.append(sum)#暫存平均
    print(A+"學生成績:")
    print("國文: "+str(row[0])+",英文: "+str(row[1])+",數學: "+str(row[2])+",自然: "+str(row[3])+",社會: "+str(row[4])+"")#輸出五科成績
    print()#換行
for i in range(0,3):
    if i==0:
        S="A"
    elif i==1:
        S="B"
    else:
        S="C"
    print(S+"學生平均成績 : "+str(ave[i]))#輸出三人平均
print()
for i in range(0,5):#輸出五科平均
    if i==0:
        x="國文"
    elif i==1:
        x="英文"
    elif i==2:
        x="數學"
    elif i==3:
        x="自然"
    else:
        x="社會"
    sum = 0
    for m in range(0,3):
        sum =sum+l[m][i]
    sum = sum/3
    print(x+"平均成績 : "+str(sum))