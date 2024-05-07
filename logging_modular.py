"""
日志记录类
"""
import datetime
import logging
import os
import shutil
from logging.handlers import RotatingFileHandler

RETAIN_MONTH = 3  # 保留X个月的日志


def delete_file(log_dir):
    """
    删除多余的日志文件
    :param log_dir:
    :return:
    """
    back_all_file_name = readfile(log_dir)

    while True:
        if len(back_all_file_name) > RETAIN_MONTH:
            # try:
            # back_all_file_name[0] = back_all_file_name[0].replace('\\\\','\\')
            # print()
            shutil.rmtree(back_all_file_name[0])
            back_all_file_name.pop(0)
            # except:
            #     pass
        else:
            break


def readfile(dir_path):
    """
    读取文件夹下的文件，不递归
    :param dir_path:
    :return:
    """
    files = os.listdir(dir_path)
    file_list = []
    for file in files:  # 遍历文件夹
        if not os.path.isdir(file):
            # file_list.append(dir_path + '/' + file)
            file_list.append(os.path.join(dir_path, file))
    return file_list


def get_current_year_month_day():
    """
    获取当前年月日
    :return:
    """
    now_time = datetime.datetime.now()
    year = str(now_time.year)
    month = str(now_time.month)
    day = str(now_time.day)
    if len(month) == 1:
        month = '0{}'.format(month)
    if len(day) == 1:
        day = '0{}'.format(day)

    now_year_month_day = '{}{}{}'.format(year, month, day)
    now_year_month = '{}{}'.format(year, month, day)

    return now_year_month, now_year_month_day


def logging_comm(log_path, log_level=logging.INFO):
    """
    :param log_path:
    :param log_level:
    :return:
    """
    log = logging.getLogger()
    # 更高级的logging特性
    log.setLevel(log_level)  # 设置过滤的日志等级
    if not log.handlers:
        # 设置日志路径, 设置日志文件最大100M， 超过100M会自动创建 log.log1文件， 最多新建100个
        handler = RotatingFileHandler(log_path, maxBytes=1024 * 1024 * 100, backupCount=100,
                                      encoding="utf-8")
        formatter = logging.Formatter("[%(asctime)s][%(filename)s] - [line:%(lineno)d] - %(levelname)s: %(message)s")
        handler.setFormatter(formatter)

        log.addHandler(handler)
    return log


source_dir = os.getcwd()
back_time, back_time_ymd = get_current_year_month_day()

year_month_dir = os.path.join(source_dir, "my_log", back_time)
os.makedirs(year_month_dir, exist_ok=True)  # 创建当年月文件

delete_file(os.path.join(source_dir, "my_log"))  # 超过指定数量的文件删除

log_path = os.path.join(year_month_dir, "log_{}.log".format(back_time_ymd))
logger_obj = logging_comm(log_path)
