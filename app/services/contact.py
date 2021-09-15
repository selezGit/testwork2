from services.exceptions import DuplicateError
from core.service import BaseService
from models import Contact
from repository import ContactRepository

from services.exceptions import UserNotFoundError
from services.user import UserService


class ContactService(BaseService):
    repository_class = ContactRepository
    _user_service = UserService()

    def create_contact(self, **data) -> Contact:
        if not self._user_service._repository.exists(id=data['user_id']):
            raise UserNotFoundError()
        if self._repository.exists(**data):
            raise DuplicateError()
        return self.create(**data)

    def update_contact(self, uid: str, **data) -> Contact:
        instance = self.get_instance(uid)
        return self.update(instance=instance, **data)

    def delete_contact(self, uid: str):
        instance = self.get_instance(uid)
        return self.destroy(instance)
