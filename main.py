# -*- coding: utf-8 -*-            
# @Author : Code_Hsy
# @Time : 2024-02-19 10:47
import time
# coding:utf-8

import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import tkinter.messagebox
import tkinter.ttk as ttk
import os
import threading

import db_do

root_path = os.path.dirname(__file__)
skills_path = os.path.join(root_path, 'rpa_skills')
skills_list = os.listdir(skills_path)


def skill_stop(exe_name='main.exe'):
    try:
        print('停止啦')
        os.system("taskkill /f /t /im {}".format(exe_name))
    except:
        print(1111)


def skill_start(skill_start_path):
    os.system(skill_start_path)


class MForm(tk.Frame):
    '''继承自Frame类，master为Tk类顶级窗体（带标题栏、最大、最小、关闭按钮）'''

    def __init__(self, master):
        super().__init__(master)

        # self.button = None
        # self.button = None
        # self.skill_label = None
        # self.kill_label = None
        self.ft = tkFont.Font(family='宋体', size=10, weight='bold')  # 创建字体
        self.initComponent(master)

    def initComponent(self, master):
        '''初始化GUI组件'''
        # 设置顶级窗体的行列权重，否则子组件的拉伸不会填充整个窗体
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)
        self.ft = tkFont.Font(family='宋体', size=10, weight='bold')  # 创建字体
        self.initMenu(master)  # 为顶级窗体添加菜单项
        # 设置继承类MWindow的grid布局位置，并向四个方向拉伸以填充顶级窗体
        self.grid(row=0, column=0, sticky=tk.NSEW)
        # 设置继承类MWindow的行列权重，保证内建子组件会拉伸填充
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.panewin = ttk.Panedwindow(self, orient=tk.HORIZONTAL)  # 添加水平方向的推拉窗组件
        self.panewin.grid(row=0, column=0, sticky=tk.NSEW)  # 向四个方向拉伸填满MWindow帧

        self.frm_left = ttk.Frame(self.panewin, relief=tk.SUNKEN, padding=0)  # 左侧Frame帧用于放置播放列表
        self.frm_left.grid(row=0, column=0, sticky=tk.NS)  # 左侧Frame帧拉伸填充
        self.panewin.add(self.frm_left, weight=1)  # 将左侧Frame帧添加到推拉窗控件，左侧权重1

        self.frm_right = ttk.Frame(self.panewin, relief=tk.SUNKEN)  # 右侧Frame帧用于放置视频区域和控制按钮
        self.frm_right.grid(row=0, column=0, sticky=tk.NS)  # 右侧Frame帧四个方向拉伸
        self.frm_right.columnconfigure(0, weight=1)  # 右侧Frame帧两行一列，配置列的权重
        self.frm_right.rowconfigure(0, weight=1)  # 右侧Frame帧两行的权重8:1
        # self.frm_right.rowconfigure(1, weight=1)
        self.panewin.add(self.frm_right, weight=50)  # 将右侧Frame帧添加到推拉窗控件,右侧权重10

        s = ttk.Style()
        # s.configure('www.TFrame', background='black')  # 视频区Frame帧添加样式
        s.configure('www.TFrame')  # 视频区Frame帧添加样式
        # 右侧Frame帧第一行添加视频区Frame
        self.frm_vedio = ttk.Frame(self.frm_right, relief=tk.RIDGE, style='www.TFrame')
        self.frm_vedio.grid(row=0, column=0, sticky=tk.NSEW)
        # 右侧Frame帧第二行添加控制按钮
        self.frm_control = ttk.Frame(self.frm_right, relief=tk.RAISED)  # 四个方向拉伸
        self.frm_control.grid(row=1, column=1, sticky=tk.NSEW)
        # self.initCtrl()  # 添加滑块及按钮
        self.frm_div = ttk.Frame(self.frm_right, relief=tk.RAISED)  # 四个方向拉伸
        self.frm_div.grid(row=0, column=1, sticky=tk.NSEW)
        self.frm_right.rowconfigure(0, weight=1)
        self.frm_div2 = ttk.Frame(self.frm_right, relief=tk.RAISED)  # 四个方向拉伸
        self.frm_div2.grid(row=0, column=2, sticky=tk.NSEW)
        self.frm_right.rowconfigure(0, weight=1)

        self.initPlayList()  # 添加树状视图

    def initMenu(self, master):
        '''初始化菜单'''
        mbar = tk.Menu(master)  # 定义顶级菜单实例

        fmenu = tk.Menu(mbar, tearoff=False)  # 在顶级菜单下创建菜单项
        mbar.add_cascade(label=' 设置 ', menu=fmenu, font=('Times', 12, 'bold'))  # 添加子菜单
        fmenu.add_command(label="授权", command=self.menu_click_event)
        fmenu.add_command(label="技能配置", command=self.menu_click_event)
        fmenu.add_separator()  # 添加分割线
        fmenu.add_command(label="退出", command=self.quit)

        etmenu = tk.Menu(mbar, tearoff=False)
        mbar.add_cascade(label=' 定时 ', menu=etmenu)
        etmenu.add_command(label="定时任务", command=self.menu_click_time_event)
        # for each in ['复制', '剪切', '合并']:
        #     etmenu.add_command(label=each, command=self.menu_click_event)
        master.config(menu=mbar)  # 将顶级菜单注册到窗体

    def menu_click_event(self):
        '''菜单事件'''
        pass

    def menu_click_time_event(self):
        '''菜单事件'''

        time_box = ODeskInput()

    def initPlayList(self):
        def treeview_click(event):
            # print('单击')

            item_text = ''
            for item in tree.selection():
                item_text = tree.item(item, "text")
                print(item_text)  # 输出所选行的第一列的值
                b['state'] = "normal"
            b['text'] = "执行-" + item_text

        def status_start(event):
            root3.deiconify()
            root.withdraw()
            # time.sleep(15)
            # start_click()

            # start_click()

        def start_click(skill_name='点击'):
            if skill_name == '点击':
                skill_name = str(b['text']).replace('执行-', '')
            skill_start_path = skills_path + '\\' + skill_name + '\\main.exe'

            # thread2 = threading.Thread(target=status_start)
            # thread2.start()
            # time.sleep(15)
            if os.path.exists(skill_start_path):
                try:
                    thread1 = threading.Thread(target=skill_start, args=(skill_start_path,))
                    thread1.start()
                    thread1.join()

                    root.deiconify()

                    root3.withdraw()
                    skill_stop()
                except:

                    root.deiconify()

                    root3.withdraw()
                    skill_stop()
                    print('技能入口程序无法启动')
            else:

                print('没有这个技能或技能入口程序丢失')
                time.sleep(10)
                root.deiconify()

                root3.withdraw()
                skill_stop()

        '''初始化树状视图'''
        self.frm_left.rowconfigure(0, weight=10)  # 左侧Frame帧行列权重配置以便子元素填充布局
        self.frm_left.columnconfigure(0, weight=1)  # 左侧Frame帧中添加树状视图
        style = ttk.Style()
        style.configure("A1.Label", font=("黑体", 11), rowheight=50)
        tree = ttk.Treeview(self.frm_left, selectmode='browse', show='tree', padding=[50],
                            style="A1.Label", )
        tree.grid(row=0, column=0, sticky=tk.NSEW)  # 树状视图填充左侧Frame帧
        tree.column('#0', width=120)  # 设置图标列的宽度，视图的宽度由所有列的宽决定

        # 一级节点parent='',index=第几个节点,iid=None则自动生成并返回，text为图标右侧显示文字
        # values值与columns给定的值对应
        # tr_root = tree.insert("", 0, None, open=True, text='技能列表')  # 树视图添加根节点
        for each in skills_list:
            tr_skill = tree.insert("", 0, None, open=True, text=each)
            # gg = tree.insert(tr_skill, 0, None, open=True, text="运行")
        # self.skill_label = ttk.Frame(self.frm_right, relief=tk.RAISED, height=200, width=400)
        # self.skill_label.grid(row=0, column=0, ipadx=50, ipady=20)
        b = tk.Button(self.frm_right, text="请选择技能执行", state="disabled")
        b.grid(row=0, column=0, ipadx=50, ipady=20)
        # b.columnconfigure(4, weight=40)
        tree.bind('<ButtonRelease-1>', treeview_click)
        b.bind('<ButtonRelease-1>', status_start)

    # def initCtrl(self):
    #     '''初始化控制滑块及按钮'''
    #     self.frm_control.columnconfigure(0, weight=1)  # 配置控制区Frame各行列的权重
    #     self.frm_control.rowconfigure(0, weight=1)  # 第一行添加滑动块
    #     self.frm_control.rowconfigure(1, weight=1)  # 第二行添加按钮
    #     # slid = ttk.Scale(self.frm_control, from_=0, to=900, command=self.sliderValueChanged)
    #     # slid.grid(row=0, column=0, sticky=tk.EW, padx=2)  # 滑动块水平方向拉伸
    #     #
    #     # frm_but = ttk.Frame(self.frm_control, padding=2)  # 控制区第二行放置按钮及标签
    #     # frm_but.grid(row=1, column=0, sticky=tk.EW)
    #     # self.lab_curr = ttk.Label(frm_but, text="00:00:00", font=self.ft)  # 标签显示当前时间
    #     # lab_max = ttk.Label(frm_but, text="00:00:00", font=self.ft)  # 标签显示视频长度
    #     # self.lab_curr.grid(row=0, column=0, sticky=tk.W, padx=3)
    #     # lab_max.grid(row=0, column=13, sticky=tk.E, padx=3)
    #     # i = 4
    #     # for but in ['播放', '暂停', '快进', '快退', '静音']:
    #     #     ttk.Button(frm_but, text=but).grid(row=0, column=i)
    #     #     i += 1
    #     # for i in range(14):  # 为每列添加权重值以便水平拉伸
    #     #     frm_but.columnconfigure(i, weight=1)

    # def sliderValueChanged(self, val):
    #     '''slider改变滑块值的事件'''
    #     # tkinter.messagebox.showinfo("Message", "message")
    #     flt = float(val)
    #     strs = str('%.1f' % flt)
    #     self.lab_curr.config(text=strs)


class Page_2(tk.Frame):  # 这是第二个页面
    def __init__(self, window):
        super().__init__(window)
        # self.initComponent(window)

        self.window = window
        self.window.title("技能运行中")
        self.window.geometry("100x50-20-80")
        self.window.config(bg="#0F375A")
        stop_button = tk.Button(self.window, text="停止", command=self.back, font=('黑体', 14, 'bold'))
        stop_button.grid(row=0, column=0, sticky=tk.NSEW, ipadx=24, ipady=10)
        #
        # def initPlayList(self):
        stop_button = tk.Button(self.window, text="停止", command=self.back, font=('黑体', 14, 'bold'))
        stop_button.grid(row=0, column=0, sticky=tk.NSEW, ipadx=24, ipady=10)
        # stop_button.bind('<ButtonRelease-1>', skill_stop)

    def back(self):
        # pass  # 不知道怎么写，先占位
        # self.quit()
        skill_stop()
        root.deiconify()

        root3.withdraw()
        # Page_1(root)


class ODeskInput(tk.Frame):
    def __init__(self):
        super().__init__()
        # self.initComponent(window)

        root4 = tk.Tk()
        self.window = root4
        self.window.title("定时设置")
        self.window.geometry('300x300')

        for i in range(len(skills_list)):
            l1 = Label(self.window, text="技能:")
            l1.grid(row=2 * i, column=0)  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
            l2 = Label(self.window, text=skills_list[i])
            l2.grid(row=2 * i, column=1)  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
            l3 = Label(self.window, text="定时:")
            l3.grid(row=2 * i + 1, column=0)  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM

            xls_text = StringVar()
            xls = Entry(self.window, textvariable=xls_text)
            xls_text.set("")
            xls.grid(row=2 * i + 1, column=1)

        # l1 = Label(self.window, text="定时crontab编码")
        # l1.grid(row=0, column=0)  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
        # xls_text = StringVar()
        # xls = Entry(self.window, textvariable=xls_text)
        # xls_text.set(" ")
        # xls.grid(row=1, padx=80)


def on_closing():
    root.quit()
    root3.quit()


def on_closing_run():
    pass


def start_do():
    for each in skills_list:
        db_do.select_all()

def loop_act():
    pass


if __name__ == '__main__':
    def status_end():
        root.deiconify()

        root3.withdraw()


    root3 = tk.Tk()
    go_app = Page_2(root3)
    root3.attributes("-toolwindow", 1)  # 去掉窗口最大化最小化按钮，只保留关闭
    root3.wm_attributes('-topmost', True)
    root3.protocol("WM_DELETE_WINDOW", on_closing_run)
    root3.option_add("*Font", "微软雅黑", 14)
    root3.withdraw()
    # root3.mainloop()
    root3.resizable(False, False)
    root = tk.Tk()
    # root2 = tk.Tk()
    root.geometry('800x480+200+100')
    style = ttk.Style()
    style.configure("A1.tittle", font=("黑体", 10))
    root.title('hRobot')
    root.option_add("*Font", "微软雅黑")
    root.minsize(800, 480)
    app = MForm(root)
    # pp = Page_2(root2)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    thread1 = threading.Thread(target=skill_start)
    thread1.start()
    thread1.join()
    root.mainloop()
