from core.service import BaseService
from models import User
from repository import UserRepository
from werkzeug.security import check_password_hash, generate_password_hash
from services.exceptions import DuplicateEmailError, DuplicateUserError, UserNotFoundError, WrongPasswordError


class UserService(BaseService):
    repository_class = UserRepository

    def register(self, login: str, email: str, password: str) -> User:
        """Register new user."""
        self.check_user_exists(email, login)

        password_hash = self._generate_password_hash(password)
        user = self.create(
            login=login,
            password=password_hash,
            email=email,
        )
        return user

    def recovery(self, email: str) -> User:
        """Recovery user account."""
        user = self.get_by_email(email)
        if not user:
            raise UserNotFoundError()
        return user

    def change_credentials(self, user: User, new_password: str):
        """Change user password."""
        self._repository.change_password_by_id(
            user.id,
            self._generate_password_hash(new_password),
        )

    def check_user_exists(self, email: str, login: str):
        if self.exists_by_login(login):
            raise DuplicateUserError()

        if self.exists_by_email(email):
            raise DuplicateEmailError()

    def login(self, login: str, password: str):
        """Login user."""
        user = self.get_by_login(login)
        if not user:
            raise UserNotFoundError()
        self.check_password(user, password)
        return self.authenticate()

    def authenticate(self) -> dict:
        """TODO test function"""
        return {'status': 'success'}

    def exists_by_login(self, login: str) -> bool:
        return self._repository.exists(login=login)

    def exists_by_email(self, email: str) -> bool:
        return self._repository.exists(email=email)

    def get_by_login(self, login: str) -> User:
        return self._repository.get_by_login(login)

    def get_by_email(self, email: str) -> User:
        return self._repository.get_by_email(email)

    def check_password(self, user: User, password: str) -> bool:
        if not check_password_hash(user.password, password):
            raise WrongPasswordError()
        return True

    @staticmethod
    def _generate_password_hash(password: str) -> str:
        return generate_password_hash(password)
