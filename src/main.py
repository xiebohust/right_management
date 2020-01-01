"""
user,role,permission,role_to_permission
增删改查


permission
id,desc,func，module
1,添加用户，add，src.auth.user


创建权限
开发执行模块下的函数
写相应的功能
角色添加权限

"""

import importlib



#
# module_name = 'src.user'
# m = importlib.import_module(module_name)
# print(m) #<module 'src.user' from '/Users/apple/PycharmProjects/fanshe/src/user.py'>
#
# # m 就是模块 user了
# m.add()
#
#
#
# func_name = 'get'
# func = getattr(m,func_name)
# func()


permission_list = [
    {'desc':'添加用户','func':'add','module':'user'},
    {'desc': '删除用户', 'func': 'delete','module':'role'},
    {'desc': '查看用户', 'func': 'get','module':'role'},

]

while True:
    for index,item in enumerate(permission_list,1):
        print(index,item)

    choice = input('choose :')
    choice = int(choice)
    # 函数名
    func_name = permission_list[choice-1]['func']

    # 模块名
    module_name = permission_list[choice-1]['module']
    # 动态导入模块
    m = importlib.import_module('src.'+module_name)

    func = getattr(m,func_name)
    func()