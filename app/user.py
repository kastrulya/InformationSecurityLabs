__author__ = 'bubble'


class User:
    """ class User """

    def __init__(self, name, password, enabled = True, password_restriction = False, role = "USER"):
        self.name = name
        self.password = password
        self.enabled = bool(int(enabled))
        self.password_restriction = bool(int(password_restriction))
        self.role = role

    def to_string(self, delimiter_data):
        return self.name + delimiter_data + self.password + delimiter_data + \
               str(int(self.enabled)) + delimiter_data + str(
            int(self.password_restriction)) \
               + delimiter_data + self.role

    def to_array(self):
        arr = []
        arr.append(self.name)
        arr.append(self.password)
        arr.append(str(int(self.enabled)))
        arr.append(str(int(self.password_restriction)))
        arr.append(self.role)
        return arr
