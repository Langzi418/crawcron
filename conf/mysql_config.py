import pymysql
from pymysql import escape_string

host = '127.0.0.1'
user = 'root'
password = '19961010'
port = 3306
db = 'ai' # 和前端保持一致, mutimodal...
table = '爬取中文文章'


def insert_db(params):
    data_base = pymysql.connect(host=host, user=user, password=password,
                                port=port, db=db)
    cursor = data_base.cursor()
    success = True
    try:
        # id自增， 文章url是唯一索引，以此来去重
        param_str = 'null,' + ','.join(["'%s'" % escape_string(param) for param in params])
        sql = "INSERT INTO %s VALUES (%s)" % (table, param_str)
        cursor.execute(sql)
        data_base.commit()
    except Exception as e:
        print(e)
        success = False
    finally:
        cursor.close()
        data_base.close()

    return success


def select_db(source, num):
    """

    :param source: 爬取来源
    :param num: 数量
    :return: 更新的数据
    """
    data_base = pymysql.connect(host=host, user=user, password=password,
                                port=port, db=db)
    cursor = data_base.cursor()
    try:
        sql = f"SELECT * FROM {table} WHERE source = '{source}' ORDER BY id DESC LIMIT {num}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        data_base.close()
