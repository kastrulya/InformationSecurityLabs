__author__ = 'bubble'
# import datastore
from DAO import file_user_DAO_impl

user_store = file_user_DAO_impl.FileUserDAO()
user_store.start_connection()


def authorize(username="", password=""):
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


def save_changes():
    pass


def add_new_user():
    pass


def logout():
    pass


def validate_password(name, password):
    return name != password
