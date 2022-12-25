import matplotlib.pyplot as plt
import numpy as np
#我三張圖程式碼一開始分開寫，所以可能會有重疊的程式碼
#第一張圖
path = 'Temperature.txt'
fp=open(path,"r") #傳送txt的內容到字典
line = fp.readline()
a = 0
b = []
c = []
## 用 while 逐行讀取檔案內容，直至檔案結尾
while line:
    temp = line
    temp = temp.replace("\n","")
    if a==0:
        b.append(temp)
    else :
        c.append(temp)
    line = fp.readline()
    a+=1
 
fp.close()

for i in range(len(c)):
    temp = str(c[i])
    temp = temp.split(',')
    d = int(temp[0])#取年份
    temp.pop(0)#去掉\n
    for j in range(len(temp)):
        temp[j] = float(temp[j])
    num = np.arange(1,13)#產生1到12的矩陣
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])#設定x,y軸單位
    plt.yticks([16,18,20,22,24,26,28,30])
    plt.plot(num, temp, label=d)#畫折線圖

plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')#標題
plt.xlabel('Month')#x軸標題
plt.ylabel('Temperature in Degree C')#y軸標題
plt.legend(loc=8)#圖例位置
plt.savefig('lab13_01.png')#存圖片

plt.clf()#清空畫布
#第二張圖
path = 'Temperature.txt'
fp=open(path,"r") #傳送txt的內容到字典
line = fp.readline()
a = 0
b = []
c = []
## 用 while 逐行讀取檔案內容，直至檔案結尾
while line:
    temp = line
    temp = temp.replace("\n","")
    if a==0:
        b.append(temp)
    else :
        c.append(temp)
    line = fp.readline()
    a+=1
 
fp.close()

e = []
f = []
g = []
for i in range(len(c)):
    temp = str(c[i])
    temp = temp.split(',')
    d = int(temp[0])
    temp.pop(0)
    for j in range(len(temp)):
        temp[j] = float(temp[j])#到這邊為止同第一張圖
        f.append(temp[j])#將所有溫度存起來
for i in range(0,12):#算12月份平均
    temp1 = 0
    for j in range(0,9):
        temp1 += f[i+12*j]
    temp1 = temp1/9
    temp1 = round(temp1,2)
    g.append (temp1)
ava = 0
for i in range(len(g)):#總溫度平均
    ava +=g[i]
ava = ava/len(g)
num = np.arange(1,13)
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])#x軸單位
plt.ylim(16, 32)#y軸單位
plt.axhline(y=ava, c="r", ls="--", lw=1.5,label=" Mean of 9 years")#畫平均那條虛線
plt.plot(num, g,marker='o',markeredgecolor='r',markerfacecolor='r')#畫折線
plt.plot(num, g,c='steelblue')#將藍色線穿過紅點
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')#標題
plt.xlabel('Month')#x軸標題
plt.ylabel('Temperature in Degree C')#y軸標題
plt.legend(loc=1)#圖例位置
for x, y in zip(num, g):#標示各月份溫度
    plt.text(x, y+0.1, y, fontsize=10)
plt.text(1,25,24.92,fontsize=10)#標示虛線溫度
plt.savefig('lab13_02.png')#存檔

plt.clf()#清空
#第三張圖
fig = plt.figure(figsize=(15,6))
fig.add_subplot(1, 2, 1)#產生子圖
plt.subplot(1, 2, 1)#畫第一張子圖
path = 'Temperature.txt'
fp=open(path,"r") #傳送txt的內容到字典
line = fp.readline()
a = 0
b = []
c = []
## 用 while 逐行讀取檔案內容，直至檔案結尾
while line:
    temp = line
    temp = temp.replace("\n","")
    if a==0:
        b.append(temp)
    else :
        c.append(temp)
    line = fp.readline()
    a+=1
 
fp.close()
e = []
f = []
g = []
for i in range(len(c)):
    temp = str(c[i])
    temp = temp.split(',')
    d = int(temp[0])
    temp.pop(0)
    for j in range(len(temp)):
        temp[j] = float(temp[j])
        f.append(temp[j])
    num = np.arange(1,13)
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    plt.yticks([16,18,20,22,24,26,28,30])
    plt.plot(num, temp, label=d)
    #print (d)
    #print (temp)

plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend(loc=8)

plt.subplot(1, 2, 2)#畫第二張子圖
path = 'Temperature.txt'
fp=open(path,"r") #傳送txt的內容到字典
line = fp.readline()
a = 0
b = []
c = []
## 用 while 逐行讀取檔案內容，直至檔案結尾
while line:
    temp = line
    temp = temp.replace("\n","")
    if a==0:
        b.append(temp)
    else :
        c.append(temp)
    line = fp.readline()
    a+=1
 
fp.close()

e = []
f = []
g = []
for i in range(len(c)):
    temp = str(c[i])
    temp = temp.split(',')
    d = int(temp[0])
    temp.pop(0)
    for j in range(len(temp)):
        temp[j] = float(temp[j])
        f.append(temp[j])
for i in range(0,12):
    temp1 = 0
    for j in range(0,9):
        temp1 += f[i+12*j]
    temp1 = temp1/9
    temp1 = round(temp1,2)
    g.append (temp1)
ava = 0
for i in range(len(g)):
    ava +=g[i]
ava = ava/len(g)
num = np.arange(1,13)
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.ylim(16, 32)
plt.axhline(y=ava, c="r", ls="--", lw=1.5,label=" Mean of 9 years")
plt.plot(num, g,marker='o',markeredgecolor='r',markerfacecolor='r')
plt.plot(num, g,c='steelblue')
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend(loc=1)
for x, y in zip(num, g):
    plt.text(x, y+0.1, y, fontsize=10)
plt.text(1,25,24.92,fontsize=10)
plt.tight_layout()#將兩張圖取正確間隔
plt.savefig('lab13_03.png')#存檔