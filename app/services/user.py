from core.service import BaseService
from models import User
from repository import UserRepository
from werkzeug.security import check_password_hash, generate_password_hash
from services.exceptions import DuplicateEmailError, DuplicateUserError, UserNotFoundError, WrongPasswordError


class UserService(BaseService):
    repository_class = UserRepository

    def register(
        self,
        login: str,
        email: str,
        password: str,
    ) -> User:
        if self.exists_by_login(login):
            raise DuplicateUserError()

        if self.exists_by_email(email):
            raise DuplicateEmailError()

        password_hash = self._generate_password_hash(password)
        self.create(
            login=login,
            password=password_hash,
            email=email,
        )
        return self.authenticate()

    def login(self, login: str, password: str) -> User:
        user = self.get_by_login(login)
        if not user:
            raise UserNotFoundError()
        self.check_password(user, password)
        return self.authenticate()

    def authenticate(self) -> dict:
        return {'status': 'success'}

    def exists_by_login(self, login: str) -> bool:
        return self._repository.exists(login=login)

    def exists_by_email(self, email: str) -> bool:
        return self._repository.exists(email=email)

    def get_by_login(self, login: str) -> User:
        return self._repository.get_by_login(login)

    def check_password(self, user: User, password: str) -> bool:
        if not check_password_hash(user.password, password):
            raise WrongPasswordError()
        return True

    @staticmethod
    def _generate_password_hash(password: str) -> str:
        return generate_password_hash(password)
