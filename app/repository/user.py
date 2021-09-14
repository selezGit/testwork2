from core.repository import BaseRepository
from models import User


class UserRepository(BaseRepository):
    model = User

    def get_by_login(self, login: str) -> User:
        return self._get_one_by_query(self.session.query(self.model).filter(self.model.login == login))
