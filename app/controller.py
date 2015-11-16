# import user_service
import session
import user_service
import view

__author__ = 'bubble'


class Controller:
    def __init__(self, root):
        self.current_session = session.Session()
        self.app_view = view.View(root)
        # self.user_service = datastore.Datastore()

    def start(self):
        self.app_view.authorize_form("Authorization", self.auth)

    def auth(self, event=""):
        data = self.app_view.get_auth_data()
        name = data["name"]
        password = data["password"]
        try:
            user = user_service.authorize(name, password)
            self.current_session.start_session(user)
            if self.current_session.current_user.role == "ADMIN":
                self.app_view.admin_form()
            else:
                self.app_view.user_form(self.logout, self.change_password)
        except ValueError as e:
            self.app_view.show_message(e.message)

    def logout(self):
        pass

    def change_password(self):
        data = self.app_view.get_data_change_password()
        old_password = data["old_password"]
        new_password = data["new_password"]
        try:
            user_service.change_password(
            self.current_session.current_user, old_password,
            new_password)
        except ValueError as e:
            self.app_view.show_message(e.message)
