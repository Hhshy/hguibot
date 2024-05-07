import contextlib
import pymysql
from pymysql.err import DataError
from logging_modular import logger_obj


# MySQL工具
class DBTools:
    def ignore_errors(func):
        def wrapper(*args, **kwargs):
            with contextlib.suppress(Exception):
                func(*args, **kwargs)

        return wrapper

    def __init__(self, host, port, user, password, db):
        self.connect = pymysql.connect(host=host, user=user, password=password, port=port)
        self.cursor = self.connect.cursor()
        self.db = db

        # 检查数据库是否存在，不存在则创建
        if not self.exists_db(db):
            self.execute(f"CREATE DATABASE {db} CHARSET utf8mb4; ")
            print(f"数据库已创建：{db}")

        self.execute(f"USE {self.db};")

    def exists_db(self, db):
        dbs = [i[0] for i in self.execute("SHOW DATABASES;")]
        return db in dbs

    def exists_table(self, table):
        self.execute(f"USE {self.db};")
        tables = [i[0] for i in self.execute("SHOW TABLES;")]
        return table in tables

    def execute(self, sql):
        self.cursor.execute(sql)
        self.connect.commit()
        return self.cursor.fetchall()

    def create(self, table_name, columns_dict: dict):

        sql = f"CREATE TABLE {table_name} ( id INT PRIMARY KEY AUTO_INCREMENT, "
        for column, col_type in columns_dict.items():
            sql += f"{column} {col_type},"
        sql = f'{sql.rstrip(",")});'
        logger_obj.debug(sql)
        return self.execute(sql)

    # @ignore_errors
    def insert(self, table, items: dict):
        """
        插入一行数据
        :param table:
        :param items:{col: val}
        :return:
        """
        # 插入前数据表表存在检查
        self.connect.ping()
        if not self.exists_table(table):
            columns_dict = {key: "VARCHAR(255)" for key in items}
            self.create(table, columns_dict)
            print(f"创建数据表成功: {table}")

        # 构建插入sql语句
        cols, values = items.keys(), items.values()
        column = ",".join(cols)
        value = "".join(f"'{i}'," for i in values).rstrip(",")
        sql = f"INSERT INTO {table} ({column}) VALUES ({value});"
        print(table, column, value)
        logger_obj.debug(sql)
        try:
            return self.execute(sql)
        except DataError as e:
            logger_obj.error(f"插入数据失败, {e}")

    @ignore_errors
    def select(self, from_table, column, target) -> tuple:
        from pymysql.err import ProgrammingError
        self.connect.ping()
        sql = f"SELECT * FROM {from_table} WHERE {column}='{target}' LIMIT 1;"
        logger_obj.debug(sql)
        try:
            return self.execute(sql)
        except ProgrammingError as e:
            if "doesn't exist" in e.__str__():
                return ()
            else:
                raise ProgrammingError(e)

    def close(self):
        self.connect.close()
        print("数据库连接已关闭！")

    ignore_errors = staticmethod(ignore_errors)


# class RedisTools:
#     def ignore_errors(func):
#         def wrapper(*args, **kwargs):
#             try:
#                 func(*args, **kwargs)
#             except ConnectionError as e:
#                 if not e.__str__().__contains__("连接尝试失败"):
#                     raise e
#
#         return wrapper
#
#     def __init__(self, host, port, password):
#         self.host = host
#         self.port = port
#         self.password = password
#         self.coon = redis.Redis(host=host, port=port, password=password, decode_responses=True, charset="utf-8")
#
#     def __auto_restart(self):
#         if not self.coon.ping():
#             self.__init__(
#                 host=self.host,
#                 port=self.port,
#                 password=self.password
#             )
#
#     def del_all_keys(self):
#         self.__auto_restart()
#         for key in self.coon.keys():
#             self.coon.delete(key)
#             log.debug(f"Redis Del Key: {key}")
#
#     def visit_count(self, add_id):
#         self.__auto_restart()
#         self.coon.incr(add_id)
#
#     # @ignore_errors
#     def get(self, key):
#         self.__auto_restart()
#         return self.coon.get(key)
#
#     def close(self):
#         self.coon.close()
#
#     ignore_errors = staticmethod(ignore_errors)
