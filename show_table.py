"""
在表格中快速定位到特定的样式

1. 数据的定位  findItems 返回一个列表   如果没查到，列表为空
2.如果找到了满足条件的单元格，会定位到单元格所在的行 setSliderPosition(row)

# 三个步骤
1.在表格里面显示很多的数据
2.通过findItems来找到所有满足条件的单元格
3.通过setSliderPosition(row)定位到满足条件的这一行
"""

import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor, QBrush


class DataLocation(QWidget):
    def __init__(self):
        super(DataLocation, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle('台账')
        # 设置窗口尺寸
        self.resize(800, 600)

        # 创建水平布局
        layout = QHBoxLayout()

        # 创建QTableWidget控件
        tableWidget = QTableWidget()
        row_num = 20
        list_data_type = ['序号', '银行卡号', '姓名', '身份证号', '银行名称', '最近导入时间', '开始止付时间',
                          '结束止付时间', '最近止付时间', '最近止付到期时间', '操作']
        dict_all = {}
        for ii in range(row_num):
            dict_show = {}
            dict_show['序号'] = str(ii + 1)
            dict_show['银行卡号'] = '银行卡号' + str(ii)
            dict_show['姓名'] = '姓名' + str(ii)
            dict_show['身份证号'] = '身份证号' + str(ii)
            dict_show['银行名称'] = '银行名称' + str(ii)
            dict_show['最近导入时间'] = '最近导入时间' + str(ii)
            dict_show['开始止付时间'] = '开始止付时间' + str(ii)
            dict_show['结束止付时间'] = '结束止付时间' + str(ii)
            dict_show['最近止付时间'] = '最近止付时间' + str(ii)
            dict_show['最近止付到期时间'] = '最近止付到期时间' + str(ii)
            dict_show['操作'] = '操作' + str(ii)
            dict_all[str(ii + 1)] = dict_show

        print(dict_all)
        # 给tableWidget设置行
        tableWidget.setRowCount(row_num)
        # 给tableWidget设置列
        tableWidget.setColumnCount(len(list_data_type))

        # 将控件添加到布局里
        layout.addWidget(tableWidget)

        # 对行循环 对列循环
        for i in range(row_num):
            for j in range(len(list_data_type)):
                # 得到每个单元格的内容
                itemContent = dict_all[str(i + 1)][list_data_type[j]]
                # 把内容放到表格中
                tableWidget.setItem(i, j, QTableWidgetItem(itemContent))

        # 搜索满足条件的Cell
        text = '(13,1)'
        # 精确搜索
        items = tableWidget.findItems(text, QtCore.Qt.MatchExactly)
        if len(items) > 0:
            items = items[0]
            # 设置背景色
            items.setBackground(QBrush(QColor(0, 255, 0)))
            items.setForeground(QBrush(QColor(255, 0, 0)))

            # 获得当前项所在的行
            row = items.row()
            # 定位到指定的行
            # verticalScrollBar 获得滚动条
            tableWidget.verticalScrollBar().setSliderPosition(row)
        # 搜索满足条件的Cell
        text = '(1'
        # MatchStartsWit 以..开头
        items = tableWidget.findItems(text, QtCore.Qt.MatchStartsWith)
        if len(items) > 0:
            items = items[0]
            # 设置背景色
            items.setBackground(QBrush(QColor(0, 255, 0)))
            items.setForeground(QBrush(QColor(255, 0, 0)))

            # 获得当前项所在的行
            row = items.row()
            # 定位到指定的行
            # verticalScrollBar 获得滚动条
            tableWidget.verticalScrollBar().setSliderPosition(row)

        # 应用于布局
        self.setLayout(layout)


if __name__ == '__main__':
    # app实例化 传参
    app = QApplication(sys.argv)
    # 创建对象
    example = DataLocation()
    # 创建窗口
    example.show()
    # 进入主循环
    sys.exit(app.exec_())
