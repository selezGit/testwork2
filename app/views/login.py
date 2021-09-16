import sys

from core.mixins import ViewMixin
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from services.exceptions import UserNotFoundError


class LoginScreen(QMainWindow, ViewMixin):
    def __init__(self):
        super().__init__()
        self.title = 'App'
        self.top = 300
        self.left = 150
        self.width = 1200
        self.height = 800
        self.InitUI()

    def InitUI(self):
        loadUi('styles/login.ui', self)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.login.clicked.connect(self.loginfn)
        self.create.clicked.connect(self.create_onClick)
        self.showpass.clicked.connect(self.change_password_mode)
        self.recover.clicked.connect(self.recover_onClick)
        self.show()

    def change_password_mode(self):
        self.passwordfield.setEchoMode(
            QtWidgets.QLineEdit.Normal if self.showpass.isChecked() else QtWidgets.QLineEdit.Password
        )

    def loginfn(self):
        login = self.emailfield.text()
        password = self.passwordfield.text()
        if self.check_fields(login=login, password=password):
            try:
                self.user_service.login(login, password)
                self.error.setText('')
                self.info.setText('Successfully logged in.')
            except UserNotFoundError:
                self.info.setText('')
                self.error.setText('Invalid username or password')


def start_app():
    app = QApplication(sys.argv)
    _ = LoginScreen()
    sys.exit(app.exec_())
