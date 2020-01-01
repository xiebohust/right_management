from src.repository import user,role,permission,role_to_perm

def add():
    username = input('username:')
    password = input('pasdword:')
    user.UserRepository().insert(username,password)

def get():
    username = input('username:')
    password = input('pasdword:')
    user.UserRepository().get_one_by_user_pwd(username,password)

def delete():
    print('user.delete')