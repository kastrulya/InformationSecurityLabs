from abc import ABCMeta, abstractmethod

__author__ = 'bubble'


class UserDAO():
    __metaclass__ = ABCMeta

    # @abstractmethod
    # def start_connection(self):
    #     raise NotImplementedError()

    @abstractmethod
    def get_users(self):
        raise NotImplementedError()

    @abstractmethod
    def add_user(self):
        raise NotImplementedError()

    @abstractmethod
    def update_user_field(self, username, field, new_data):
        raise NotImplementedError()

    @abstractmethod
    def delete_user(self, username):
        raise NotImplementedError()

    @abstractmethod
    def find_user_by_name(self, username):
        raise NotImplementedError()

    @abstractmethod
    def save_changes(self):
        raise NotImplementedError()
