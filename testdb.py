
import pymysql

conn = pymysql.connect(host='120.27.112.240', port=3306, user='root',
                                    passwd="wq12345678", db="douban_movice"
                                    # , charset="utf-8"
                                    # ,cursorclass=pymysql.cursors.DictCursor
                       )

cur = conn.cursor()
cur.execute("SELECT * FROM top250_movice")
# print(cur.fetchall())

for row in cur.fetchall():
    print("Test: " + row.__str__())

conn.close()