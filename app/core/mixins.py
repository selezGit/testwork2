
from PyQt5.QtWidgets import QDialog
from services import ContactService, UserService


class ViewMixin(QDialog):
    user_service = UserService()
    contact_service = ContactService()

    def login_onClick(self):
        from views import LoginScreen  # noqa

        self.cams = LoginScreen()
        self.cams.show()
        self.close()

    def create_onClick(self):
        from views import CreateAccScreen  # noqa

        self.cams = CreateAccScreen()
        self.cams.show()
        self.close()

    def recover_onClick(self):
        from views import RecoverAccScreen  # noqa

        self.cams = RecoverAccScreen()
        self.cams.show()
        self.close()

    def check_fields(self, **kwargs) -> bool:
        not_exists = [key for key, value in kwargs.items() if not value]
        if not_exists:
            self.error.setText(f'Please input: {", ".join(not_exists)}')
            return False
        return True

    def check_passwords_fields(self, password_1, password_2) -> bool:
        if password_1 != password_2:
            self.error.setText('Passwords do not match.')
            return False
        return True
