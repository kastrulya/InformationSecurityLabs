import time

__author__ = 'bubble'


class Session:
    """ class Session, save info about current session """

    def __init__(self):
        self.current_user = ""

    def start_session(self, current_user):
        self.current_user = current_user
        self.start_time_session = time.time()

    def stop_session(self):
        self.current_user = ""
        self.start_time_session = ""


