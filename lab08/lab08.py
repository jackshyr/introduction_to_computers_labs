import os
a = os.getcwd()#讀入當前目錄
a = a.split("/")
a.remove('')
print(a)
path = 'E94111229.txt'
b = open (path,'w')
c = 0
for file in a:
    b.write(a[c])
    b.write(os.linesep)
    c+=1
c = 0
path1 = os.sep+"home"+os.sep+"E94111229"#讀入home目錄
a = os.listdir(path1)
print (a)
b.write(os.linesep)
for file in a:
    b.write(a[c])
    b.write(os.linesep)
    c+=1
b.close()

