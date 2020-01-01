from src.util.db_handler import Mysql

obj = Mysql()
obj.connect()

class Role(object):


    def get_all(self):
        pass



    def get_one_by_id(self,id):
        sql = 'select * from role where id=%s'
        return obj.execute(sql,(id,))


    def insert(self,name):
        sql = 'insert into role (name) values(%s)'
        return obj.execute(sql, (name,))


    def update(self):
        pass

    def delete(self):
        pass



if __name__ == '__main__':
    Ro = Role()
    Ro.insert('删除用户')
    print(Ro.get_one_by_id(1))

