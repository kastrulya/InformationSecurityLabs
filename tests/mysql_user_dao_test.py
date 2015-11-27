import random
import string
import unittest
from DAO.mysql_user_DAO_impl import MySQLUserDAO
from app.user import User

__author__ = "bubble"


class MySQLUserDaoTestCase(unittest.TestCase):
    def test_get_users(self):
        storage = MySQLUserDAO()
        all_users = storage.get_users()
        # self.assertEqual(len(all_users), 7,
        #                  str(len(all_users)) + "!=2")
    #
    # def test_append_new_user(self):
    #     storage = MySQLUserDAO()
    #     start_length = len(storage.get_users())
    #     N = 5
    #     name = ''.join(random.choice(string.ascii_letters) for _ in range(N))
    #     password = ''.join(
    #         random.choice(string.ascii_uppercase + string.ascii_letters) for _
    #         in range(N))
    #     user = User("bubble", password, '1', '0', "USER")
    #     storage.add_user(user)
    #     finish_length = len(storage.get_users())
    #     self.assertEqual(start_length + 1, finish_length,
    #                      "wrong number of users after adding new one")
    #
    # def test_update_field(self):
    #     storage = MySQLUserDAO()
    #     name = 'bubble'
    #     field = 'password'
    #     new_data = ''.join(
    #         random.choice(string.ascii_uppercase + string.ascii_letters) for _
    #         in range(5))
    #     storage.update_user_field(name, field, new_data)
    #     all_users = storage.get_users()
    #     for i in range(0, len(all_users)):
    #         if (all_users[i].name == name):
    #             curr_user = all_users[i]
    #             break
    #     print curr_user.password
    #     self.assertEqual(curr_user.password, new_data, curr_user.password + "!=" + new_data + ": changes aren't saved")

    def test_delete_user(self):
        storage = MySQLUserDAO()
        data = storage.get_users()
        user_to_delete = data[-1].name
        start_length = len(data)
        storage.delete_user(user_to_delete)
        finish_length = len(storage.get_users())
        self.assertEqual(start_length - 1, finish_length,
                         "wrong number of users after deleting one")

if __name__ == "__main__":
    unittest.main()
