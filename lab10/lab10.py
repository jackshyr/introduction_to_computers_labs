# 複製就對了
from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# web server 路由設定
# 若有get request傳送到 / ，就會執行他下面的這個function，function名稱隨意，但不可重複
@app.route('/',methods=['GET'])
def root():
    return 'ok' # 發送response body 為 ok

# 將webserver執行，監聽任意來源ip，port開在3000，開啟debug模式
# debug模式代表，每次檔案更新後，webserver會自動重啟，不需要手動重啟
dic0 ={}
@app.route('/set',methods=['POST'])
def root1():
    data = request.form.to_dict()
    b = data.values()
    c = list(b)
    if c[0] in dic0:
        return "key exist"
    else:
        dic0.update({c[0]:c[1]})
        return "set success"
@app.route('/key_list',methods=['GET'])
def root2():
    a = dic0.keys()
    a = list(a)
    return str(a)
@app.route('/get_value/<key>',methods=['GET'])
def root3(key):
    if key in dic0:
        return dic0.get(key)
    else:
        return"key not found"
@app.route('/update_value',methods=['POST'])
def root4():
    data1 = request.form.to_dict()
    b = data1.values()
    c = list(b)
    if c[0] in dic0:
        dic0[c[0]] =c[1]
        return "update success"
    else:
        return "key does not exist"
@app.route('/delete/<key>',methods=['GET'])
def root5(key):
    if key in dic0:
        del dic0[key]
        return "delete success"
    else:
        return"key not found"
app.run(host="0.0.0.0", port=3000, debug=True)
