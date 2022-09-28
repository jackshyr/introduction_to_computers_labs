for i in range(0,3):
    if i==0:
        A="A"
    elif i==1:
        A="B"
    else i==2:
        A="C"
    print("開始輸入"+A+"學生的成績,請依照國文,英文,數學,自然,社會 的順序輸入:")
    a =[]
    All =[][]
    for j in range(0,5):
        a.append(input(int()))
        All[i][j]=a[j]
