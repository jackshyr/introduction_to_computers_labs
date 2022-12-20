#PIC/S GMP藥廠名單資料集
#https://data.fda.gov.tw/opendata/exportDataList.do?method=ExportData&InfoId=31&logType=5
import pymysql
import  json, ssl, urllib.request

url = 'https://data.fda.gov.tw/opendata/exportDataList.do?method=ExportData&InfoId=31&logType=5'
context = ssl._create_unverified_context() #用api讀入檔案

with urllib.request.urlopen(url, context=context) as jsondata:
    #將JSON進行UTF-8的BOM解碼，並把解碼後的資料載入JSON陣列中
     data = json.loads(jsondata.read().decode('utf-8-sig')) 
a = 0 #計數
b = [] #分別存四個欄位的東東
c = []
d = []
e = []
for i in data: #將檔案存入
    #print(type(i['類別']),'\t',type(i['名稱']),'\t',type(i['地址']),'\t',type(i['GMP核定作業內容']),'\t')
    b.append(i['類別'])
    c.append(i['名稱'])
    d.append(i['地址'])
    e.append(i['GMP核定作業內容'])
    a +=1
    if a>9:
        break
    #,i['備註'],'\t'

connect_db = pymysql.connect(host='localhost', port=3306, user='E94111229', passwd='0522', charset='utf8', db='wordpress') #設定連接

cursor = connect_db.cursor() #將名字縮寫並定義游標

for i in range(0,10): #將10筆資料上傳到資料庫中
    sqlStuff ="INSERT INTO P(class,name,address,gmpcontent)VALUES(%s, %s, %s, %s)"#(助教能告訴我為什麼資料表名稱用PIC/S GMP藥廠名單資料集會syntax error嗎)
    records = (b[i],c[i],d[i],e[i])
    # 執行 SQL 指令
    #cursor.execute("""INSERT INTO PIC/S GMP藥廠名單資料集 values (%s,%s,%s,%s)"""%(b[i],c[i],d[i],e[i]))
    cursor.execute(sqlStuff,records)
    
# 提交至 SQL
connect_db.commit()

# 關閉 SQL 連線
connect_db.close()
