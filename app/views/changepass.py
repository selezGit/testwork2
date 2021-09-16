from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from models import User
from core.mixins import ViewMixin


class ChangePassScreen(ViewMixin):
    def __init__(self, user: User):
        super(ChangePassScreen, self).__init__()
        self._user = user
        loadUi('styles/changepass.ui', self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.changepass.clicked.connect(self.recoverfn)
        self.back.clicked.connect(self.recover_onClick)

    def recoverfn(self):
        password = self.passwordfield.text()
        confirmpassword = self.confirmpasswordfield.text()
        if self.check_fields(password=password, confirmpassword=confirmpassword):
            if self.check_passwords_fields(password, confirmpassword):
                self.user_service.change_credentials(self._user, password)
                self.info.setText('Password changed successfully')