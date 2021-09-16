from core.mixins import ViewMixin
from PyQt5.uic import loadUi
from services.exceptions import UserNotFoundError


class RecoverAccScreen(ViewMixin):
    title = 'recover'

    def __init__(self):
        super(RecoverAccScreen, self).__init__()
        loadUi('styles/recoveracc.ui', self)
        self.changepass.clicked.connect(self.recoverfn)
        self.back.clicked.connect(self.login_window)

    def recoverfn(self):
        email = self.emailfield.text()
        if self.check_fields(email=email):
            try:
                user = self.user_service.recovery(email)
                self.changepass_window(user)
            except UserNotFoundError:
                self.error.setText(f'User {email} not found')
