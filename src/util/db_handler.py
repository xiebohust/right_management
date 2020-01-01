import pymysql

class Mysql:

    def __init__(self, host='localhost',user='root',password='',
                 database='test',port=3306,charset='utf8',cursorclass=pymysql.cursors.DictCursor):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset
        self.cursorclass = cursorclass
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = pymysql.connect(self.host,self.user,self.password,self.database,
                                    self.port,charset=self.charset,cursorclass=self.cursorclass)
        except:
            print('connection failed')
            return False
        else:
            self.cursor = self.conn.cursor()
            return True

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


    def execute(self,sql,params=None):
        if self.conn and self.cursor:
            self.cursor.execute(sql,params)
            self.conn.commit()
            data = self.cursor.fetchone()
            return data


if __name__ == '__main__':
    obj = Mysql()
    obj.connect()
    # r = obj.execute('create table permission '
    #                 '(id int(10) primary key auto_increment,'
    #                 'name varchar(20),'
    #                 'func varchar(20),'
    #                 'module varchar(20))'
    #                 )
    # 建表

    # r = obj.execute('create table role '
    #                 '(id int(10) primary key auto_increment,'
    #                 'name varchar(20))'
    #                 )
    #
    # r = obj.execute('create table role_to_perm '
    #                 '(id int(10) primary key auto_increment,'
    #                 'role_id int(10),'
    #                 'perm_id int(10))'
    #                 )
    # print(r)

