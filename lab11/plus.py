import json

def check(a,b,mid,length):
    sum = 0 
    count = 0
    for i in range(length): 
        if (sum+a[i])>mid: #如果總重量加當前的重量超過給定條件，次數加一，並將sum重製
            sum = a[i]
            count += 1
        else:
            sum += a[i]
    if sum: #將最後那批人的次數加上去
        count += 1
    return (count>b)
with open('input_plus.json', 'r') as inputFile: #讀檔
    data = json.load(inputFile) # load data
    for key in data:
        input1 = data[key]
        a = input1[0] #體重
        b = input1[1] #次數
        l = 0
        r = 50000
        length = len(a)
        while l<=r:   #二分搜尋法
            if (l+r)%2 == 0: #無條件捨去取整數
                mid = (l+r)/2
            else:
                mid = (l+r-1)/2
            if check(a,b,mid,length): #若目前次數大於給定次數，則mid過小，需移動左界
                l = mid + 1
            else:
                r = mid - 1
        print('Question: ' + str(key))
        print('Assignment:', int(l))   
    
