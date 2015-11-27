import MySQLdb
import app
from app.user import User
from user_DAO import UserDAO
from app.security import Security
__author__ = 'bubble'


class MySQLUserDAO(UserDAO):
    def __init__(self, user='root', password='root'):
        self.database = "user_management"
        self.users_table = "User"
        self.host = 'localhost'
        self.user = user
        self.password = password

    def get_users(self):
        sql = 'SELECT * from ' + self.database + '.' + self.users_table
        data = self.execute_sql(sql)
        all_users = [User(*user) for user in data]
        if (len(all_users) == 0):
            user = User("admin", "admin", role='ADMIN')
            self.add_user(user)
            self.get_users()
        return all_users

    def add_user(self, user):
        sql = "INSERT INTO " + self.users_table + " VALUES (" + \
                  self.user_to_string(user) + ")"
        self.execute_sql(sql)

    def update_user_field(self, username, field, new_data):
        sql = "UPDATE User SET  " + field + " = " + "'" + new_data + "'" + " WHERE name = '" + username + "'"
        self.execute_sql(sql)

    def delete_user(self, username):
        sql = "DELETE FROM " + self.users_table + " WHERE name = '" + username + "'"
        self.execute_sql(sql)

    def find_user_by_name(self, username):
        all_users = self.get_users()
        founded_user = [user for user in all_users if user.name == username]
        if (len(founded_user)):
            return founded_user[0]
        else:
            return

    def save_changes(self):
        raise NotImplementedError()

    def execute_sql(self, sql):
        # Open database connection
        db = MySQLdb.connect(self.host, self.user, self.password,
                             self.database)

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
            return cursor.fetchall()
        except:
            # Rollback in case there is any error
            db.rollback()

        # disconnect from server
        db.close()

    @staticmethod
    def user_to_string(user):
        user_arr = user.to_array()
        user_str = "\"" + "\",\"".join(user_arr) + "\""
        return user_str