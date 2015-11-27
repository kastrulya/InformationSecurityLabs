from DAO import file_user_DAO_impl
from DAO import mysql_user_DAO_impl
from user import User

__author__ = 'bubble'


# user_store = file_user_DAO_impl.FileUserDAO()
# user_store.start_connection()

user_store = mysql_user_DAO_impl.MySQLUserDAO('admin', 'admin')


def authorize(username="", password=""):
    users = user_store.get_users()
    if user_store.find_user_by_name(username):
        find_user = user_store.find_user_by_name(username)
        if find_user.password == password:
            return find_user
        else:
            raise ValueError("Password is wrong")
    else:
        raise ValueError("User doesn't exist")


def change_password(user, old_password, new_password):
    if user.password != old_password:
        raise ValueError("Wrong old password!")
    elif not is_password_valid(user, new_password):
        raise ValueError("New password is invalid")
    else:
        user_store.update_user_field(user.name, "password", new_password)


def is_password_valid(user, new_password):
    valid = True if not user.password_restriction or validate_password(
        user.name, new_password) else False
    return valid


def save_changes(blocked_user, restriction_password_user):
    for name in blocked_user:
        user_store.update_user_field(
            name,
            "enabled",
            not blocked_user[name].get()
        )

    for name in restriction_password_user:
        user_store.update_user_field(
            name,
            "password_restriction",
            restriction_password_user[name].get()
        )


def add_new_user(name):
    user = User(name, name)
    user_store.add_user(user)

def logout():
    pass


def validate_password(name, password):
    return name != password
