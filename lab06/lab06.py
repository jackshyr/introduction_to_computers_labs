def gcd(a,b):
    if a==0 or b==0:#判斷兩者是否為0
        print("0沒有gcd")
    else:
        d = a#紀錄原先的值
        e = b
        while True:#找最大公因數
            a = a%b
            if a==0 or b==0:
                break
            b = b%a
            if a==0 or b==0:
                break
        c = a+b
        if c==1:#判斷是否互質
            print(str(d)+"和"+str(e)+"互質")
        else:
            print (str(d)+"和"+str(e)+"的gcd="+str(c))
ans1 = gcd(80,20)
ans2 = gcd(10,0)
ans3 = gcd(19,20)

