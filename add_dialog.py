# -*- coding: utf-8 -*-            
# @Author : Code_Hsy
# @Time : 2024-02-02 10:24

from PyQt5.QtWidgets import *


class AddDialog(QDialog):
    def __init__(self, parent=None):
        super(AddDialog, self).__init__(parent)
        self.init_ui(parent)

    def init_ui(self, parent):
        '''水平布局'''
        hbox = QHBoxLayout()

        self.save_btn = QPushButton()
        self.save_btn.setText('保存')
        self.save_btn.clicked.connect(lambda: self.save_btn_click(parent))

        self.cancel_btn = QPushButton()
        self.cancel_btn.setText('取消')
        self.cancel_btn.clicked.connect(self.cancel_btn_click)

        hbox.addWidget(self.save_btn)
        hbox.addWidget(self.cancel_btn)

        '''表单布局'''
        fbox = QFormLayout()

        self.seq_lab = QLabel()
        self.seq_lab.setText('序号：')
        self.seq_text = QLineEdit()
        self.seq_text.setPlaceholderText('请输入序号')

        self.name_lab = QLabel()
        self.name_lab.setText('姓名：')
        self.name_text = QLineEdit()
        self.name_text.setPlaceholderText('请输入姓名')

        self.age_lab = QLabel()
        self.age_lab.setText('年龄：')
        self.age_text = QLineEdit()
        self.age_text.setPlaceholderText('请输入年龄')

        self.class_lab = QLabel()
        self.class_lab.setText('班级：')
        self.class_text = QLineEdit()
        self.class_text.setPlaceholderText('请输入班级')

        self.socre_lab = QLabel()
        self.socre_lab.setText('表现：')
        self.socre_text = QLineEdit()
        self.socre_text.setPlaceholderText('请输入表现')

        fbox.addRow(self.seq_lab, self.seq_text)
        fbox.addRow(self.name_lab, self.name_text)
        fbox.addRow(self.age_lab, self.age_text)
        fbox.addRow(self.class_lab, self.class_text)
        fbox.addRow(self.socre_lab, self.socre_text)

        vbox = QVBoxLayout()
        vbox.addLayout(fbox)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def save_btn_click(self, parent):
        if self.seq_text.text().strip() != '' and self.name_text.text().strip() != '' \
                and self.age_text.text().strip() != '' and self.class_text.text().strip() != '' \
                and self.socre_text.text().strip() != '':
            print(parent.data_list)
            data = [self.seq_text.text(),
                    self.name_text.text(),
                    self.age_text.text(),
                    self.class_text.text(),
                    self.socre_text.text()]
            parent.data_list.append(data)
            print(parent.data_list)
            parent.query_data_list()
            self.close()

    def cancel_btn_click(self):
        self.close()

    @staticmethod
    def get_add_dialog(parent=None):
        dialog = AddDialog(parent)
        return dialog.exec()
