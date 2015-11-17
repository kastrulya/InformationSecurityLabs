import tkFileDialog
from Tkinter import *
import tkMessageBox
import ttk

__author__ = 'bubble'


class InstallerView:
    def __init__(self, root):
        self.root = root

    def main_form(self, install_app_func):
        self.root.title("Setup")
        self.root.geometry("350x150")
        label = Label(self.root, text="Install programm")
        label.grid(columnspan=2)
        self.label_path = Label(self.root, text="Choose directory for installing program: ")
        self.label_path.grid(row=3, column=0, pady=15)

        button_choose_directory = Button(self.root, text="Folder")
        button_choose_directory['command'] = self.ask_file_name
        button_choose_directory.grid(row=3, column=1)

        counter = IntVar()
        self.progress_bar = ttk.Progressbar(
            self.root,
            orient=HORIZONTAL,
            length=300,
            mode='determinate',
            variable=counter, maximum=40
        )
        self.progress_bar.grid(pady=10, padx=10, columnspan=2)

        button_setup = Button(self.root, text="Setup")
        button_setup['command'] = lambda: self.install_action(install_app_func)
        button_setup.grid(columnspan=2)

    def ask_file_name(self):
        dirname = tkFileDialog.askdirectory(
            parent=self.root,
            initialdir="/",
            title='Please select a directory to install'
        )
        if len(dirname) > 0:
            self.selected_folder = dirname
            self.label_path["text"] = dirname

    def get_dir_to_install(self):
        return self.selected_folder

    def install_action(self, install_app_func):
        self.progress_bar.start()
        install_app_func()

    def stop_install(self):
        self.progress_bar.stop()

    def show_message(self, message):
        message = tkMessageBox.showinfo("", message)