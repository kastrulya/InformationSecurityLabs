from unittest import TestLoader, TextTestRunner, TestSuite
from file_user_dao_test import FileUserDaoTestCase

if __name__ == '__main__':
    fooSuite = TestLoader().loadTestsFromTestCase(FileUserDaoTestCase)

    fooRunner = TextTestRunner()
    fooResult = fooRunner.run(fooSuite)