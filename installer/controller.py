import view
from utils import install_service
__author__ = 'bubble'


class Controller:
    def __init__(self, root):
        self.install_view = view.InstallerView(root)

    def start(self):
        self.install_view.main_form(self.install_app)

    def install_app(self):
        try:
            path_to_install = self.install_view.get_dir_to_install()
            install_service.install_app(path_to_install)
            self.install_view.stop_install()
            self.install_view.show_message("Programm is installed!")
        except AttributeError as err:
            message = "Check folder, please"
            self.install_view.show_message(message)
            self.install_view.stop_install()
        except:
            self.install_view.show_message("You have already installed programm there. Check it")
            self.install_view.stop_install()
