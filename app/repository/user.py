from core.repository import BaseRepository
from models import User


class UserRepository(BaseRepository):
    model = User

    def get_by_login(self, login: str) -> User:
        return self._get_one_by_query(self.session.query(self.model).filter(self.model.login == login))

    def get_by_email(self, email: str) -> User:
        return self._get_one_by_query(self.session.query(self.model).filter(self.model.email == email))

    def change_password_by_id(self, uid, password):
        self.session.query(User).filter(User.id == uid).update({User.password: password})
