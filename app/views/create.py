from core.mixins import ViewMixin
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from services.exceptions import DuplicateEmailError, DuplicateUserError


class CreateAccScreen(ViewMixin):
    title = 'register'

    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi('styles/createacc.ui', self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfn)
        self.back.clicked.connect(self.login_window)

    def signupfn(self):
        login = self.loginfield.text()
        email = self.emailfield.text()
        password = self.passwordfield.text()
        confirmpassword = self.confirmpasswordfield.text()

        if self.check_fields(
            username=login,
            email=email,
            password=password,
            confirmpassword=confirmpassword,
        ):
            if self.check_passwords_fields(password, confirmpassword):
                try:
                    self.user_service.register(login=login, email=email, password=password)
                    self.profile_window()
                except DuplicateUserError:
                    self.error.setText(f'Login {login} exists')

                except DuplicateEmailError:
                    self.error.setText(f'Email {email} exists')
