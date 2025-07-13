import pymysql

def run_query(sql):
    DB_HOST = 'attendance-db2.c94gwgoa2ir1.eu-west-2.rds.amazonaws.com'
    DB_USER = 'admin'
    DB_PASS = 'ccgroup11'
    DB_NAME = 'attendance'

    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()

    return result
