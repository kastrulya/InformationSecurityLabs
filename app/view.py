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
        self.root.password = Entry(self.root, show="*")

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

    def user_form(self, logout_func, change_password_func,
                  title="User management"):
        self.form = self.new_window(title, width=600, height=400)
        self.logout_button(logout_func)
        self.change_password(change_password_func)

    def admin_form(self, logout_func, change_password_func, users,
                   save_changes_func, add_user_func, title="Administrator"):
        self.user_form(logout_func, change_password_func,
                       title)
        self.user_list(users, save_changes_func, add_user_func)

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

    def logout_button(self, logout_func):
        button = Button(self.form, text="Log out")
        button["command"] = lambda: self.logout_action(logout_func)
        button.grid()
        return button

    def logout_action(self, logout_func):
        self.form.destroy()
        self.root.deiconify()
        logout_func()

    def get_user_changes(self):
        return {
            "blocked_users": self.var_block_user,
            "restriction_password_users": self.var_restriction_password
        }

    def get_new_user_data(self):
        return self.new_username.get()

    def user_list(self, users, save_changes_func, add_user_func):
        Label(self.form, text="List of users").grid(row=5, column=0)
        Label(self.form, text="Block user").grid(row=5, column=1)
        Label(self.form, text="Password restriction").grid(row=5, column=2)

        row_number = 6
        column_block = 1
        column_restriction = 2
        self.var_block_user = {}
        self.var_restriction_password = {}

        for user in users:
            label_name = Label(self.form, text=user.name)
            label_name.grid(sticky=W, column=0)

            self.var_block_user[user.name] = IntVar()
            self.var_restriction_password[user.name] = IntVar()

            block_user = Checkbutton(self.form,
                                     variable=self.var_block_user[user.name])
            if user.role == "ADMIN":
                block_user["state"] = "disabled"
            if not user.enabled:
                block_user.select()
            block_user.grid(row=row_number, column=column_block)
            restriction_password = Checkbutton(
                self.form, variable=
                self.var_restriction_password[user.name]
            )
            if user.password_restriction:
                restriction_password.select()
            restriction_password.grid(row=row_number,
                                      column=column_restriction)
            row_number += 1

        bttn_save_changes = Button(self.form, text="Update list")
        bttn_save_changes["command"] = save_changes_func
        bttn_save_changes.grid()

        bttn_add_user = Button(self.form, text="Add new user")
        bttn_add_user["command"] = lambda: self.add_user(add_user_func)
        bttn_add_user.grid(pady=20)

    def add_user(self, add_user_func):
        form = self.new_window("Add user", 300, 100)
        Label(form, text="Username: ").grid(row=0, column=0)
        self.new_username = StringVar()
        new_username_form = Entry(form, textvariable=self.new_username)
        new_username_form.grid(row=0, column=1)
        bttn_add = Button(form, text="Add new user")
        bttn_add["command"] = lambda: self.add_user_action(add_user_func, form)
        bttn_add.grid(column=1, sticky=E)

    def add_user_action(self, add_user_func, close_window):
        close_window.destroy()
        add_user_func()

    @staticmethod
    def show_message(message):
        tkMessageBox.showinfo("", message)
