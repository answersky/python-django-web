import MySQLdb


def connectMysql():
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "123", "test", charset='utf8')
    return db

