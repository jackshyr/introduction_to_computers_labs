# -*- coding: UTF-8 -*-
number = input("please input a number:")#輸入數字 
number = int(number)#將字串轉成數字
if(number%2==1):#如果他是奇數
    print("this is odd")#輸出他是奇數
else:#其他
    print("this is even")#輸出他是偶數
a = input("please input your student ID first character:")#輸入開頭字母
b = input("please input your student ID last 8 numbers:")#輸入後8位數字
c  = int(b)#轉換成數字型態
if(c%2==1):#如果他是奇數
    print("your student ID is odd")#輸出他是奇數
else:#其他
    print("your student ID is even")#輸出他是偶數
ID = a+b#將英文與數字組合
print("your student ID is:"+ID)#輸出ID



