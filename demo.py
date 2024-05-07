# -*- coding: utf-8 -*-            
# @Author : Code_Hsy
# @Time : 2024-01-31 16:59

import flask, json

# print(__name__)
server = flask.Flask(__name__)  # __name__代表当前的python文件，把当前这个python文件，当成一个服务


def my_db(sql):
    import pymysql
    coon = pymysql.connect(host='xx.xx.xx.xx', user='jxz', passwd='123456', port=3306, db='jxz', charset='utf8')
    cur = coon.cursor()
    cur.execute(sql)
    if sql.strip()[:6].upper() == 'SELECT':  # 判断sql语句是否select开头
        res = cur.fetchall()  # 获取到sql语句所有的返回结果
    else:
        coon.commit()
        res = 'ok'
    cur.close()
    coon.close()
    return res


@server.route('/index', methods=['get'])  # 装饰器  ip:8080/index?xxx
def index():
    res = {'msg': '这个是我开发的第一个接口', 'msg_code': 0}  # 这个是字典，接口返回的是json，所以需要引入json，并且返回进行json.dumps
    return json.dumps(res, ensure_ascii=False)  # 返回结果是unicode，需要增加ensure_ascii=False


@server.route('/reg', methods=['post'])
def reg():
    username = flask.request.values.get('username')
    pwd = flask.request.values.get('passwd')
    if username and pwd:
        sql = 'select * from my_user WHERE username="%s";' % username
        if my_db(sql):
            res = {'msg': '用户已存在！', 'msg_code': 2001}
        else:
            insert_sql = 'insert into my_user(username,passwd,is_admin)values("%s","%s",0);' % (username, pwd)
            my_db(insert_sql)
            res = {'msg': '注册成功！', 'msg_code': 0}
    else:
        res = {'msg': '必填字段未填，请检查接口文档！', 'msg_code': 1001}
    return json.dumps(res, ensure_ascii=False)


server.run(port=7777, debug=True,
           host='0.0.0.0')  # 端口号要是不指定，默认为5000.debug=True,改了代码之后不用重启，会自动重启一次。后面增加host='0.0.0.0'，别人可以访问
