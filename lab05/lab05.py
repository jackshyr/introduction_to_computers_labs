subject = ['國文','英文','數學','自然','社會']
gradeA = ['50','60','70','80','90']
gradeB = ['57','86','73','82','43']
gradeC = ['97','96','86','97','83']
dic0 = {"index":subject,"StuA":gradeA,"StuB":gradeB,"StuC":gradeC}
for i in dic0:
    print(i)
    print(dic0[i])
l = []
l.append(gradeA)
l.append(gradeB)
l.append(gradeC)
#print (l)
for i in range(0,3):
    sum = 0
    if i==0:
        s="A"
    elif i==1:
        s="B"
    else:
        s="C"
    for j in range(0,5):
        if i==0:
            sum = sum+int(gradeA[j])
        elif i==1:
            sum = sum+int(gradeB[j])
        else :
            sum = sum+int(gradeC[j])
       # print ("Test")
    sum/=5
    print(s+"學生平均成績 :"+str(sum))
print()
for i in range(0,5):
    sum = 0
    if i==0:
        s="國文"
    elif i==1:
        s="英文"
    elif i==2:
        s="數學"
    elif i==3:
        s="自然"
    else:
        s="社會"
    for j in range(0,3):
        sum = sum+int(l[j][i])
    sum/=3
    print(s+"平均成績 :"+str(sum))
