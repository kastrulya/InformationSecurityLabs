from Tkinter import *
import tkMessageBox

__author__ = 'bubble'


class View:
    """ class View """

    def __init__(self, root):
        self.root = root

    @staticmethod
    def window_settings(window, width, height):
        pass

    def get_auth_data(self):
        return {
            "name": self.root.name.get(),
            "password": self.root.password.get()
        }

    def authorize_form(self, title, auth_func):
        self.root.title(title)
        label = Label(self.root, text="Input your name && password, please")
        label.grid(columnspan=2)

        self.root.name = Entry(self.root)
        self.root.password = Entry(self.root)

        self.root.count = 0
        self.root.current_user = ""

        self.root.name.grid()
        self.root.password.grid()

        self.root.button_submit = Button(self.root, text="Enter")
        self.root.name.bind("<Return>", auth_func)
        self.root.password.bind("<Return>", auth_func)
        self.root.button_submit["command"] = auth_func
        self.root.button_submit.grid()

    def new_window(self, title, width=100, height=100):
        window = Toplevel(self.root)
        window.title(title)
        self.window_settings(self.root, width, height)
        self.root.withdraw()
        return window

    def user_form(self, logout_func, change_password_func, title="User management"):
        self.form = self.new_window(title, width=600, height=400)
        self.logout(logout_func)
        self.change_password(change_password_func)

    def admin_form(self):
        pass

    def get_data_change_password(self):
        return {
            "old_password": self.form.entry_old_password.get(),
            "new_password": self.form.entry_new_password.get()
        }

    def change_password(self, change_password_func):
        label_old_password = Label(self.form, text="Old password")
        label_new_password = Label(self.form, text="New password")
        self.form.entry_old_password = Entry(self.form)
        self.form.entry_new_password = Entry(self.form)
        button_confirm = Button(self.form, text="Change password")
        label_old_password.grid(sticky=W)
        self.form.entry_old_password.grid(row=1, column=1)
        label_new_password.grid(sticky=W)
        self.form.entry_new_password.grid(row=2, column=1)
        button_confirm.grid(column=1, sticky=E)
        button_confirm["command"] = change_password_func

    def logout(self, logout_func):
        button = Button(self.form, text="Log out")
        button["command"] = logout_func
        button.grid()
        return button

    def user_list(self, save_changes_func):
        pass

    def add_user(self, add_user_func):
        pass

    @staticmethod
    def show_message(message):
        tkMessageBox.showinfo("", message)
