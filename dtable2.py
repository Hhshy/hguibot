# -*- coding: utf-8 -*-            
# @Author : Code_Hsy
# @Time : 2024-02-02 10:23

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from add_dialog import AddDialog


class DataManage(QWidget):
    def __init__(self):
        super(DataManage, self).__init__()
        self.data_list = []
        self.init_ui()

    def init_ui(self):
        '''全局设置'''

        self.setWindowIcon(QIcon('数据.ico'))
        self.setWindowTitle('数据管理器')
        self.resize(550, 400)
        grid = QGridLayout()

        '''菜单设置'''

        self.add_btn = QPushButton()
        self.add_btn.setText('添加数据')
        self.add_btn.clicked.connect(self.add_btn_click)

        self.del_btn = QPushButton()
        self.del_btn.setText('删除数据')
        self.del_btn.clicked.connect(self.del_data_row)

        self.query_btn = QPushButton()
        self.query_btn.setText('查询')
        self.query_btn.clicked.connect(self.query_data_list)

        '''数据列表设置'''

        self.data_table = QTableWidget()
        COLUMN = 5
        ROW = 0
        self.data_table.setColumnCount(COLUMN)
        self.data_table.setRowCount(ROW)
        h_table_header = ['序号', '姓名', '年龄', '班级', '表现']
        self.data_table.setHorizontalHeaderLabels(h_table_header)
        self.data_table.verticalHeader().setVisible(False)
        self.data_table.setShowGrid(True)
        self.data_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.data_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.data_table.setSelectionMode(QTableWidget.SingleSelection)

        for index in range(self.data_table.columnCount()):
            headItem = self.data_table.horizontalHeaderItem(index)
            headItem.setTextAlignment(Qt.AlignVCenter)

        '''加入布局'''

        grid.addWidget(self.add_btn, 0, 0, 1, 1)
        grid.addWidget(self.del_btn, 0, 1, 1, 1)
        grid.addWidget(self.query_btn, 0, 2, 1, 1)
        grid.addWidget(self.data_table, 1, 0, 1, 3)

        self.setLayout(grid)

    # 将新增数据的按钮绑定到该槽函数
    def add_btn_click(self):
        '''
        打开新增数据的弹框模块
        :return:
        '''
        AddDialog.get_add_dialog(self)

    # 将查询数据的按钮绑定到该槽函数
    def query_data_list(self):
        '''
        查询数据、并将数据展示到主窗口的数据列表中
        :return:
        '''
        data = self.data_list
        if len(data) != 0 and len(data[0]) != 0:
            self.data_table.setRowCount(len(data))
            self.data_table.setColumnCount(len(data[0]))
            for i in range(len(data)):
                for j in range(len(data[0])):
                    self.data_table.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    # 将删除数据按钮绑定到该槽函数
    def del_data_row(self):
        '''
        删除某一行的数据信息
        :return:
        '''
        row_select = self.data_table.selectedItems()
        print(row_select)
        if len(row_select) != 0:
            row = row_select[0].row()
            print(row)
            self.data_table.removeRow(row)
            del self.data_list[row]
        print(self.data_table)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DataManage()
    main.show()
    sys.exit(app.exec_())
