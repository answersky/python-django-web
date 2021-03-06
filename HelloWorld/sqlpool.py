from DBUtils.PooledDB import PooledDB
import MySQLdb

def connectDbPool():
    # 5为连接池里的最少连接数
    pool = PooledDB(MySQLdb, 5, host='localhost', user='root', passwd='123', db='test', port=3306)
    # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
    conn = pool.connection()
    return conn