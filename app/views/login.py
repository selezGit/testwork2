import sys

from core.mixins import ViewMixin
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from services.exceptions import UserNotFoundError


class LoginScreen(ViewMixin):
    title = 'login'

    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        loadUi('styles/login.ui', self)
        self.setWindowTitle(self.title)
        self.login.clicked.connect(self.loginfn)
        self.create.clicked.connect(self.create_window)
        self.showpass.clicked.connect(self.change_password_mode)
        self.recover.clicked.connect(self.recover_window)
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
