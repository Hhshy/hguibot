# -*- coding: utf-8 -*-            
# @Author : Code_Hsy
# @Time : 2024-02-02 10:01

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from copy import copy
import sys
import pymysql

ins = "insert into student (Sno,Sname,Sage,Ssex,Stele) values ('{}','{}','{}','{}','{}');"
delete = "delete from student where Sno={}"
sel = "select * from student"
upd = "update student set Sname='{}',Sage='{}',Ssex='{}',Stele='{}' where Sno={};"


def getCursor():
    """
    :return: 返回操作数据库的cursor
    """
    conn = pymysql.connect(host='127.0.0.1'  # 连接名称，默认127.0.0.1
                           , user='root'  # 用户名
                           , passwd='admin123'  # 密码
                           , port=3306  # 端口，默认为3306
                           , db='stop_pay_data'  # 数据库名称
                           # , charset='utf8'  # 字符编码
                           )
    return conn


def ExecuSQL(argv):
    """
    执行数据库的语句,但是没有返回值
    :param argv:
    """
    conn = getCursor()
    cur = conn.cursor()  # 生成游标对象
    cur.execute(argv)  # 执行SQL语句
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接


def getData(argv):
    """
    执行数据库的语句,有返回值
    :param argv:
    """
    conn = getCursor()
    cur = conn.cursor()  # 生成游标对象
    cur.execute(argv)  # 执行SQL语句
    data = cur.fetchall()  # 通过fetchall方法获得数据
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
    return data


class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        hhbox = QHBoxLayout()  # 横向布局
        hhbox_1 = QHBoxLayout()
        vbox = QVBoxLayout()

        self.displayList = []
        self.saveList = []
        self.table = QTableWidget()

        self.addItem = QPushButton("添加数据")
        self.searchItem = QPushButton("刷新数据")
        self.deleteItem = QPushButton("删除数据")
        self.saveItem = QPushButton("保存数据")

        self.table_sitting()
        hhbox.addWidget(self.table)  # 把表格加入布局
        hhbox_1.addWidget(self.addItem)
        hhbox_1.addWidget(self.searchItem)
        hhbox_1.addWidget(self.deleteItem)
        hhbox_1.addWidget(self.saveItem)
        vbox.addLayout(hhbox)
        vbox.addLayout(hhbox_1)
        self.setLayout(vbox)  # 创建布局
        self.setWindowTitle("数据库—表格")
        # self.setWindowIcon(QIcon("icon.png"))

        self.connecter()

        self.resize(680, 600)
        self.show()

    def connecter(self):
        self.addItem.clicked.connect(self._addItem)
        self.deleteItem.clicked.connect(self._deleteItem)
        self.searchItem.clicked.connect(self._redraw)
        self.saveItem.clicked.connect(self._saveItem)
        self.table.itemChanged.connect(self._dataChanged)

    def _dataChanged(self):
        """
        一旦检测到数据改变,则进行检查,
        选择添加新数据还是对原数据进行修改
        :return:
        """
        row_select = self.table.selectedItems()
        if len(row_select) == 0:
            return
        row = row_select[0].row()
        content = (self.table.item(row, 0).text(), self.table.item(row, 1).text(),
                   self.table.item(row, 2).text(), self.table.item(row, 3).text(),
                   self.table.item(row, 4).text())

        if row <= len(self.displayList):
            print("修改行", content)
            self.displayList[row - 1] = content
        else:
            print("最新行", content)
            self.displayList.append(content)

    def _addItem(self):
        """
        添加空白行按钮的触发事件
        添加后刷新视图
        """
        num = self.table.rowCount() - 1
        self.newLine(num)
        self.update()

    def init(self):
        """
        初始化操作
        即从数据库加载数据
        """
        argv = "select * from student"
        data = getData(argv)
        print("初始化")
        for index, item in enumerate(data):
            self.newLine(index + 1, item=item)
            self.displayList.append(item)
        self.saveList = copy(self.displayList)
        self.update()

    def _redraw(self):
        """
        repaint即刷新数据,
        用保存的数据覆盖未保存的数据
        """
        self.table.setRowCount(0)
        self.table.clearContents()
        self.table_sitting(flag=0)
        for index, item in enumerate(self.saveList):
            self.newLine(index + 1, item)
        self.update()

    def _deleteItem(self):
        """
        若有选中行,点击删除后即可删除
        :return:
        """
        # ExecuSQL()
        row_select = self.table.selectedItems()
        if len(row_select) == 0:
            return
        id = row_select[0].row()
        if int(id) < len(self.displayList):
            print("删除一条数据")
            self.displayList.pop(id - 1)
        self.header.pop()
        self.table.removeRow(row_select[0].row())
        self.update()

    def _saveItem(self):
        """
        点击保存需要
        筛选出需要更新的数据
        需要删除的数据
        需要添加的数据
        """
        idList = [int(k[0]) for k in self.saveList]
        _idList = [int(k[0]) for k in self.displayList]
        print("点击保存")
        # print(self.saveList)
        # print(self.displayList)
        for item in self.displayList:
            if item not in self.saveList:
                print("存在修改数据")
                if item[0] not in idList:
                    sql = ins.format(item[0], item[1], item[2], item[3], item[4])
                    print(sql)
                    ExecuSQL(sql)
                    print("insert")
                else:
                    sql = upd.format(item[1], item[2], item[3], item[4], item[0])
                    print(sql)
                    ExecuSQL(sql)
                    print("update")
        for item in self.saveList:
            if item[0] not in _idList:
                sql = delete.format(item[0])
                print(sql)
                ExecuSQL(sql)
                print("delete", item)
        self.saveList = copy(self.displayList)

    def newLine(self, num, item=None):
        """
        :param num: 在对应序号处的序号画空白行
        :param item: 输入为对应数据
        """
        # num=self.table.rowCount()
        self.table.insertRow(num)
        _0 = QTableWidgetItem("")
        _0.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        _1 = QTableWidgetItem("")
        _2 = QTableWidgetItem("")
        _3 = QTableWidgetItem("")
        _4 = QTableWidgetItem("")
        # item=studentInfo()
        if item != None:
            _0.setText(str(item[0]))
            _1.setText(str(item[1]))
            _2.setText(str(item[2]))
            _3.setText(str(item[3]))
            _4.setText(str(item[4]))
        else:
            _0.setText(str(num))

        self.table.setItem(num, 0, _0)
        self.table.setItem(num, 1, _1)
        self.table.setItem(num, 2, _2)
        self.table.setItem(num, 3, _3)
        self.table.setItem(num, 4, _4)
        self.header.append(str(num))
        self.table.setVerticalHeaderLabels(self.header)
        self.update()

    def table_sitting(self, flag=1):
        """
        :param flag: 初始化表头和行列数
        """
        self.header = [""]
        self.table.setColumnCount(5)
        self.table.setRowCount(2)  # 设置表格有两行五列
        self.table.setItem(0, 0, QTableWidgetItem("学号"))
        self.table.setItem(0, 1, QTableWidgetItem("名字"))
        self.table.setItem(0, 2, QTableWidgetItem("出生日期"))
        self.table.setItem(0, 3, QTableWidgetItem("性别"))
        self.table.setItem(0, 4, QTableWidgetItem("电话号码"))
        if flag:
            self.init()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Example()
    sys.exit(app.exec_())
