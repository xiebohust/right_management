from src.util.db_handler import Mysql

obj = Mysql()
obj.connect()

class UserRepository(object):


    def get_all(self):
        sql = 'select * from user'
        return obj.execute(sql)


    def get_one_by_user_pwd(self,username,password):
        sql = 'select * from user where username = %s and password=%s'
        return obj.execute(sql,(username,password))


    def insert(self,username,password):
        sql = 'insert into user (username,password) values(%s, %s)'
        return obj.execute(sql, (username, password))


    def update(self):
        pass

    def delete(self):
        pass



if __name__ == '__main__':
    User = UserRepository()
    # res = User.get_all()
    # print(res)
    res1 = User.get_one_by_user_pwd('a','123')
    print(res1)
    res = User.insert('b','234')
