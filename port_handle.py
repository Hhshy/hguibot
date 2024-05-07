# -*- coding: utf-8 -*-            
# @Author : Code_Hsy
# @Time : 2023-10-13 10:32

from logging_modular import logger_obj
import requests
import datetime
import json


class WithSessionDo:
    def __init__(self):
        self.session = requests.session()

    def get(self, url, **kwargs):
        for i in range(10):
            try:
                res = self.session.get(url, **kwargs)
                res.raise_for_status()
                return res
            except Exception as e:
                logger_obj.info(f">>> GET请求异常 <<< \n请求url: {url}\n请求次数  >> {i + 1} \nexception:{e}")

    def post(self, url, **kwargs):
        for i in range(10):
            try:
                res = self.session.post(url, **kwargs)
                res.raise_for_status()
                return res
            except Exception as e:
                logger_obj.info(f">>> POST请求异常 <<< \n请求url: {url}\n请求次数  >> {i + 1} \nexception:{e}")

    def put(self, url, **kwargs):
        return self.session.put(url, **kwargs)

    def options(self, url, **kwargs):
        return self.session.options(url, **kwargs)

    def close(self):
        self.session.close()
        logger_obj.info("控制台会话已关闭！")


class WithPortDo(WithSessionDo):
    def __init__(self, port_url):
        super().__init__()
        self._headers = {}
        # self.url = 'http://127.0.0.1:80'
        self.url = port_url

    def ce_shi(self):
        print(self.url)

    def inquire_stop_pay(self):
        """
        止付查询方法
        :return:
        """

        headers = {
            'Content-Type': 'application/json;charset=utf-8',
        }

        page_num = 1
        list1 = []
        while True:

            data = {
                'pageSize': 5000,
                'pageNum': page_num
            }

            response = requests.post(self.url + "/rpa/api/v1/ledger/suspendPay/list", data=json.dumps(data),
                                     headers=headers).json()

            # response = requests.get(url + "/rpa/api/v1/system/query").json()
            # print(response['data']['pageNum'])
            is_last_page = response['data']['isLastPage']
            for item_msg in response.get('data')['list']:
                list1.append(item_msg)
            # print(is_last_page)

            if is_last_page:
                break
            else:
                page_num += 1

        # if response["code"] != '200':
        #     logger_obj.info(f"查询数据失败, status: {response['code']}")
        #     return False

        logger_obj.info(f"查询数据成功, 数据条数: {len(list1)}")
        # return姓名银行卡等数据的列表->字典
        return list1

    def add_stop_pay(self, data_in):
        """
        止付添加方法
        :return:
        """

        headers = {
            'Content-Type': 'application/json;charset=utf-8',
        }

        data = data_in
        response = self.post(self.url + "/rpa/api/v1/ledger/suspendPay/add", data=json.dumps(data),
                             headers=headers).json()

        if response["code"] != '200':
            logger_obj.info(f"添加数据失败, status: {response['code']}")
            return False

        logger_obj.info(f"添加数据成功, status: {response['code']}")
        return True

    def correct_stop_pay(self, data_in):
        """
        止付编辑方法
        :params:
            bankCardNumber	string
            必须
            银行卡号
            idCardNumber	string
            非必须
            身份证号
            bankName	string
            非必须
            银行名称
            suspendEndTime	string
            非必须
            结束止付时间
            lastSuspendTime	string
            非必须
            最近止付时间
            lastSuspendExpireTime	string
            非必须
            最近止付到期时间
        :return:
        """
        data = data_in

        headers = {
            'Content-Type': 'application/json;charset=utf-8',
        }

        response = self.post(self.url + "/rpa/api/v1/ledger/suspendPay/updateByCardNumber", data=json.dumps(data),
                             headers=headers).json()

        if response["code"] != '200':
            logger_obj.info(f"编辑数据失败, status: {response['code']}")
            return False

        logger_obj.info(f"编辑数据成功, status: {response['code']}")
        return True

    def inquire_all_search(self):
        """
        全量查查询方法
        :return:
        """

        headers = {
            'Content-Type': 'application/json;charset=utf-8',
        }

        data = {
            'lastSuspendExpireStartTime': (datetime.datetime.now() + datetime.timedelta(days=33)).strftime(
                '%Y-%m-%d %H:%M:%S'),
            'lastSuspendExpireEndTime': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        response = self.post(self.url + "/rpa/api/v1/ledger/fullQuery/listForRpa", data=json.dumps(data),
                             headers=headers).json()

        if response["code"] != '200':
            logger_obj.info(f"查询数据失败, status: {response['code']}")
            return False

        logger_obj.info(f"查询数据成功, status: {response['code']}")
        # return姓名银行卡等数据的列表->字典
        return response.get('data')

    def correct_all_search(self, data_in):
        """
        止付编辑方法
        :params:
            bankCardNumber	string
            必须
            姓名
            idCardNumber	string
            必须
            身份证号
            bankName	string
            必须
            银行名称
            status	number
            必须
            状态
        :return:
        """
        data = data_in

        headers = {
            'Content-Type': 'application/json;charset=utf-8',
        }

        response = self.post(self.url + "/rpa/api/v1/ledger/fullQuery/updateStatus", data=json.dumps(data),
                             headers=headers).json()

        if response["code"] != '200':
            logger_obj.info(f"编辑数据失败, status: {response['code']}")
            return False

        logger_obj.info(f"编辑数据成功, status: {response['code']}")
        return True

    def add_all_search(self, data_in):
        """
        止付添加方法
        :return:
        """

        headers = {
            'Content-Type': 'application/json;charset=utf-8',
        }

        data = data_in

        response = self.post(self.url + "/rpa/api/v1/ledger/fullQuery/add", data=json.dumps(data),
                             headers=headers).json()

        if response["code"] != '200':
            logger_obj.info(f"添加数据失败, status: {response['code']},data:{response['data']}")
            return False

        logger_obj.info(f"添加数据成功, status: {response['code']}")
        return True

    def activate_code_status(self):
        """
        查询授权状态
        :params:
            activateStatus 返回2为授权通过
        :return:
        """

        headers = {
            'Content-Type': 'application/json;charset=utf-8',
        }

        response = self.get(self.url + "/rpa/api/v1/activateCode/queryInfo",
                            headers=headers).json()

        if response["code"] != '200':
            logger_obj.info(f"获取授权失败, status: {response['code']}")
            return False
        if response["data"]["activateStatus"] != 2:
            logger_obj.info(f"授权过期或未授权，请联系管理员授权, status: {response['data']['activateStatus']}")
            return False

        logger_obj.info(f"授权成功, status: {response['data']['activateStatus']}")
        return True
