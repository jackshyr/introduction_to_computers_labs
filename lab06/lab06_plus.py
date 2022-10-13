import random as r
Times = {"One":0,"Two":0,"Three":0,"Four":0,"Five":0,"Six":0}
list1 = list(Times.keys())
list2 = [0,0,0,0,0,0]

for i in range(1000000):
    a = r.randint(1,6)
    list2[a-1] = list2[a-1]+1
for i in range(0,6):
    a = list2[i]
    a = a/10000
    print ("The probability of "+list1[i]+" is "+str(round(a,2))+" %")
