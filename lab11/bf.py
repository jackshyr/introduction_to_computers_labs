import json

def sequence(a): #產生一個陣列內容是1到a
    b = []
    for i in range(0,a):
        b.append(i+1)
    return b
def select(arr): #排列
    result = []
    if len(arr) == 1: #定義遞迴停止的條件
        return [arr]
    for i in range(len(arr)): #將第一位取出，後續的數字作排列
        r_element = arr[:i]+arr[i+1:]
        r_list = select(r_element)
        l = []
        for j in r_list: #補上第一位數
            l.append(arr[i:i+1]+j)
        result += l
    return result
def BF(input1):
    minimum = 10000000 #定義初始化成本
    N = len(input1)
    a = select(sequence(N))
    for i in range(len(a)): #將每組排列的成本帶入
        cost = 0
        c = a[i]
        for j in range(len(c)):
            d = input1[j]
            cost += d[c[j]-1]
        if cost < minimum: #判別是否為最小成本
            minimum = cost
            assignment = c
    for i in range(len(assignment)):
        assignment[i] -=1
    return assignment, minimum

# main
with open('input.json', 'r') as inputFile: #讀檔
    data = json.load(inputFile) # load data
    for key in data:
        input1 = data[key] # load each input

        # Brute Force Algorithm
        assignment, minimum = BF(input1)

        print('Question: ' + str(key))
        print('Assignment:', assignment)
        print('Cost:', minimum)
        print()
