import json

def check(a,b,mid):
    sum = 0 
with open('input_plus.json', 'r') as inputFile: #讀檔
    data = json.load(inputFile) # load data
    for key in data:
        input1 = data[key]
        a = input1[0] #體重
        b = input1[1] #次數
    l = 0
    r = 50000
    while l<=r:
        if (l+r)%2 == 0:
        mid = (l+r)/2
        else:
        mid = (l+r-1)/2
        if check(a,b,mid):
            r = mid - 1
        else:
            l = mid + 1
    print('Question: ' + str(key))
    print('Assignment:', l)   
    