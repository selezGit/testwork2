from typing import Type

from .repository import BaseRepository


class BaseService:
    """Base class for business logic"""

    repository_class: Type[BaseRepository]

    def __init__(self):
        self._repository = self.repository_class()

    def get_by_id(self, uid):
        return self._repository.get_by_id(uid)

    def create(self, **data):
        instance = self._repository.insert(**data)
        self._repository.session_commit()
        return instance

    def update(self, instance, **data):
        self._repository.update(instance, **data)
        self._repository.session_commit()

    def destroy(self, instance):
        self._repository.delete_by_id(instance.id)
        self._repository.session_commit()

    def all(self, **filters):
        return self._repository.all(**filters)
