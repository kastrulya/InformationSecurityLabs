import os
from app import crypto
from user_DAO import UserDAO
from app.user import User
from app.security import Security
import common.files

__author__ = 'bubble'


class FileUserDAO(UserDAO):
    def __init__(self):
        self.name_storage = "user_list.txt"
        self.path_storage = os.path.join("../bin", self.name_storage)
        self.delimiter_users = '\n'
        self.delimiter_data_user = ' '

    def create_storage(self):
        user = User("admin", "admin", 1, 0, "ADMIN")
        self.add_user(user)

    def get_data_users(self):
        data = common.files.read_from_file(self.path_storage)
        # decode file
        if not isinstance(data, Exception):
            data = Security().decode_string(data)
            users = data.split(self.delimiter_users)
            users = [user.split(self.delimiter_data_user) for user in users]
            # return users
        else:
            self.create_storage()
            users = self.get_data_users()
        return users

    def is_userstore_exist(self):
        try:
            open(self.path_storage, "r")
            return True
        except IOError:
            return False

    def get_users(self):
        all_data = self.get_data_users()
        if not all_data:
            return
        all_users = []
        for i in range(0, len(all_data)):
            user = self.convert_to_user(all_data[i])
            if user:
                all_users.append(user)
        return all_users

    def add_user(self, user):
        if self.is_userstore_exist():
            users = self.get_users()
            if self.find_user_by_name(user.name, users):
                raise ValueError('Such user exists')
            users.append(user)
            self.save_changes(users)
        else:
            users = []
            users.append(user)
            self.save_changes(users)

    def find_user_by_name(self, username):
        users = self.get_users()
        if not users:
            return
        founded_user = [user for user in users if user.name == username]
        if len(founded_user):
            return founded_user[0]
        return

    def update_user_field(self, username, field, new_data):
        users = self.get_users()
        user = self.find_user_by_name(username, users)
        setattr(user, field, new_data)
        self.save_changes(users)

    def delete_user(self, username):
        users = self.get_users()
        user = self.find_user_by_name(username)
        users.remove(user)
        self.save_changes(users)

    def save_changes(self, users):
        user_data = []
        for user in users:
            user_data.append(self.convert_to_string(user))
        users_str = self.delimiter_users.join(user_data)
        encode_users = Security().encode_string(users_str)
        common.files.overwrite_file(self.path_storage, encode_users)

    @staticmethod
    def convert_to_user(array):
        if len(array) != 5:
            return
        name = array[0]
        password = array[1]
        enabled = int(array[2])
        password_restriction = int(array[3])
        role = array[4]
        user = User(name, password, enabled, password_restriction, role)
        return user

    def convert_to_string(self, user):
        user_str = user.name + self.delimiter_data_user + user.password + self.delimiter_data_user + str(
            int(user.enabled)) + self.delimiter_data_user + str(int(
            user.password_restriction)) + self.delimiter_data_user + user.role

        return user_str