from core.mixins import ViewMixin
from PyQt5.uic import loadUi
from services.exceptions import UserNotFoundError

from views.changepass import ChangePassScreen


class RecoverAccScreen(ViewMixin):
    def __init__(self):
        super(RecoverAccScreen, self).__init__()
        loadUi('styles/recoveracc.ui', self)
        self.changepass.clicked.connect(self.recoverfn)
        self.back.clicked.connect(self.login_onClick)

    def recoverfn(self):
        email = self.emailfield.text()
        if self.check_fields(email=email):
            try:
                user = self.user_service.recovery(email)
                self.cams = ChangePassScreen(user)
                self.cams.show()
                self.close()
            except UserNotFoundError:
                self.error.setText(f'User {email} not found')
