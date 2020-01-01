from conf import settings
from src.repository.user import UserRepository
from src.repository.role import Role


current_user_permission_list = []

current_user_info = {}



def choice_menu():
    while True:
        for i,item in enumerate(current_user_permission_list,1):
            print(i,item)
        choice = input('choose:')
        choice = int(choice)
        permision = current_user_permission_list[choice-1]


def register():
    obj = UserRepository()
    if obj.exist('root'):
        print('用户存在了')
    else:
        obj.insert()


def login():
    username = input('user:')
    password = input('pass:')
    res = UserRepository().get_one_by_user_pwd(username,password)
    if res:
        current_user_info['username']=username
        current_user_info['role_id'] =res.get('role_id')

        print('current_user_info',current_user_info)
        role_id = current_user_info['role_id']
        print(role_id)
        result = Role().get_one_by_id(role_id)
        print(result)
        current_user_permission_list.append(result)

        print('current_user_permission_list:',current_user_permission_list)


        return current_user_info
    else:
        print('用户名或密码错误')



def find_pwd():
    pass

action_dict = {
    '1':login,
    '2':register,
    '3':find_pwd
}

def main_menu():
    pass


def execute():
    while True:
        print('欢迎来到权限管理系统')
        print('1。登录 2.注册 3.找回密码')
        choice = input('选择操作：')
        result = action_dict[choice]()
        if result:
            choice_menu()




if __name__ == '__main__':
    execute()



