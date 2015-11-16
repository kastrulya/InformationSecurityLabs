import os
from user_DAO import UserDAO
from app.user import User
import common.files

__author__ = 'bubble'


class FileUserDAO(UserDAO):
    def __init__(self):
        self.name_storage = "user_list.txt"
        self.path_storage = os.path.join("../bin", self.name_storage)
        self.delimiter_users = '\n'
        self.delimiter_data_user = ' '

    def start_connection(self):
        self.users = self.get_users()

    def get_data_users(self):
        data = common.files.read_from_file(self.path_storage)
        if not isinstance(data, Exception):
            all_data = common.files.read_from_file(self.path_storage)
            users = all_data.split(self.delimiter_users)
            users = [user.split(self.delimiter_data_user) for user in users]
            return users
        else:
            user = User("admin", "admin", 1, 0, "ADMIN")
            self.add_user(user)
            self.get_data_users()

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
        if self.find_user_by_name(user.name):
            raise ValueError('Such user exists')
        self.users.append(user)

    def find_user_by_name(self, username):
        founded_user = [user for user in self.users if user.name == username]
        if len(founded_user):
            return founded_user[0]
        return

    def update_user_field(self, username, field, new_data):
        user = self.find_user_by_name(username)
        setattr(user, field, new_data)

    def delete_user(self, username):
        user = self.find_user_by_name(username)
        self.users.remove(user)

    def save_changes(self):
        user_data = []
        for user in self.users:
            user_data.append(self.delimiter_data_user.join(user))
        users_str = self.delimiter_users.join(user_data)
        common.files.overwrite_file(self.path_storage, users_str)

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
