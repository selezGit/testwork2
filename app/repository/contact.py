from core.repository import BaseRepository
from models import Contact


class ContactRepository(BaseRepository):
    model = Contact
