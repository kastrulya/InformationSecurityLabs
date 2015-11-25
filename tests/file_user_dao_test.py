import unittest
from DAO.file_user_DAO_impl import FileUserDAO
from app.user import User
__author__ = "bubble"


class FileUserDaoTestCase(unittest.TestCase):
    def test_convert_to_string_user(self):
        user = User("admin", "admin", 1, 0, "ADMIN")
        file_dao = FileUserDAO()
        user_str = "admin admin 1 0 ADMIN"
        self.assertEqual(file_dao.convert_to_string(user), user_str,
                         'incorrect converting to string')


if __name__ == "__main__":
    unittest.main()
