from HelloWorld import sqlpool


def validateLoginInfo(name, pwd):
    conn = sqlpool.connectDbPool()
    cur = conn.cursor()
    sql = "select * from user where username='" + name + "'"
    cur.execute(sql)
    result = cur.fetchone()
    print(result)
    cur.close()
    conn.close()
    if result:
        validateName = result[1]
        print(validateName)
        validatePwd = result[2]
        print(validatePwd)
        if pwd == validatePwd:
            return "登录成功"
        else:
            return "密码错误"
    else:
        return "用户名不存在"

