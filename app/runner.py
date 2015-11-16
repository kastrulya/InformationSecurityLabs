from Tkinter import Tk
from controller import Controller

__author__ = 'bubble'


def run_app():
    root = Tk()
    controller = Controller(root)
    controller.start()
    root.mainloop()


run_app()
