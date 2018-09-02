#encoding=utf-8
import json
import hashlib
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)
db = pymysql.connect(host='localhost',user='root', password='MiniGame@33', port=3306, db='minigame')
cursor = db.cursor()

@app.route('/')
@app.route('/index/')
def index():
    return "hello minigame"
    
@app.route('/signup/', methods=['POST'])
def signup():
    ret_json = {}
    nickname = request.values.get('nickname')
    password = request.values.get('password')
    if (nickname is None or password is None):
        ret_json["ret"] = -1
        ret_json["msg"] = "param is none"
    else:
        sql = "select * from playerinfo where nickname = %s"
        cursor.execute(sql,(nickname))
        if (cursor.rowcount > 0):
            ret_json["ret"] = -1
            ret_json["msg"] = "this nickname is registered"
        else:
            sql = "insert into playerinfo(nickname,password) values(%s,%s)"
            try:
                cursor.execute(sql,(nickname,password))
                db.commit()
            except Exception as e:
                db.rollback()
                ret_json["ret"] = -1
                ret_json["msg"] = "db error"
                return json.dumps(ret_json)
            ret_json["ret"] = 0;
            ret_json["msg"] = "succ signup"
    
    return json.dumps(ret_json)
    
@app.route('/signin/', methods=['POST'])
def signin():
    ret_json = {}
    nickname = request.values.get('nickname')
    password = request.values.get('password')
    if (nickname is None or password is None):
        ret_json["ret"] = -1
        ret_json["msg"] = "param is none"
    else:
        sql = "select * from playerinfo where nickname=%s"
        cursor.execute(sql,(nickname))
        if (cursor.rowcount == 0):
            ret_json["ret"] = -1
            ret_json["msg"] = "no this nickname"
        else:
            dbret = cursor.fetchone()
            if (password != dbret[2]):
                ret_json["ret"] = -1
                ret_json["msg"] = "password wrong"
            else:
                ret_json["ret"] = 0
                ret_json["msg"] = "succ signin"
                ret_json["archive"] = dbret[3]
    
    return json.dumps(ret_json)
    
@app.route('/save', methods=['GET'])
def save():
    ret_json = {}
    nickname = request.args.get('nickname')
    archive = request.args.get('archive')
    if (nickname is None):
        ret_json["ret"] = -1
        ret_json["msg"] = "nickname is none"
    else:
        sql = "select * from playerinfo where nickname=%s"
        cursor.execute(sql,(nickname))
        if (cursor.rowcount == 0):
            ret_json["ret"] = -1
            ret_json["msg"] = "no this nickname"
        else:
            sql = "update playerinfo set archive = %s where nickname = %s"
            try:
                cursor.execute(sql,(archive,nickname))
                db.commit()
            except Exception as e:
                db.rollback()
                ret_json["ret"] = -1
                ret_json["msg"] = "db error"
                return json.dumps(ret_json)
            ret_json["ret"] = 0;
            ret_json["msg"] = "succ save"
            ret_json["archive"] = archive

    return json.dumps(ret_json)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2333)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    