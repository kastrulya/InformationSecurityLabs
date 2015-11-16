import os
from user import User
import common.files

__author__ = 'bubble'


class Datastore:
    """ class Datastore """

    def __init__(self):
        self.name_storage = "user_list.txt"
        self.path_storage = os.path.join("../bin", self.name_storage)
        self.delimiter_user = '\n'
        self.delimiter_data = ' '

    def get_data_users(self):
        data = common.files.read_from_file(self.path_storage)
        if not isinstance(data, Exception):
            all_data = common.files.read_from_file(self.path_storage)
            users = all_data.split(self.delimiter_user)
            users = [user.split(self.delimiter_data) for user in users]
            return users
        else:
            user = User("admin", "admin", 1, 0, "ADMIN")
            self.add_user(user)
            self.get_data_users()

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
        user_data = user.to_string(self.delimiter_data, self.delimiter_user)
        common.files.write_to_file(self.path_storage, user_data, self.delimiter_user)

    def find_user(self, username):
        users = self.get_users()
        founded_user = [user for user in users if user.name == username]
        if len(founded_user):
            return founded_user[0]
        return

    def is_user_exists(self, username):
        founded_users = self.find_user(username)
        return bool(founded_users)

    def update_list_user(self, old_data, new_data):
        all_users_data = common.files.read_from_file(self.path_storage)
        all_users_data = all_users_data.replace(old_data, new_data)
        common.files.overwrite_file(self.path_storage, all_users_data)

    def change_user_field(self, user, field, new_data):
        old_data = user.to_string(self.delimiter_data)
        setattr(user, field, new_data)
        new_data = user.to_string(self.delimiter_data)
        self.update_list_user(old_data, new_data)
