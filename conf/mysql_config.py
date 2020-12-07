import pymysql

host = '127.0.0.1'
user = 'root'
password = '19961010'
port = 3306


def insert_db(db, table, params):
    data_base = pymysql.connect(host=host, user=user, password=password,
                                port=port, db=db)
    cursor = data_base.cursor()
    success = True
    try:
        # id自增， 文章url是唯一索引，以此来去重
        param_str = 'null,' + ','.join(["'%s'" % param for param in params])
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


def select_db(db, table, num):
    data_base = pymysql.connect(host=host, user=user, password=password,
                                port=port, db=db)
    cursor = data_base.cursor()
    try:
        sql = f'select * from {table} ORDER BY id desc LIMIT {num}'
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        data_base.close()


if __name__ == '__main__':
    select_db('ai', 'jiqizhixin', 11)
