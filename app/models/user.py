import uuid

from db import Model
from sqlalchemy import VARCHAR, Column, String
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship


class User(Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(
        'id',
        VARCHAR(length=36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False,
    )
    login = Column(String(length=255), unique=True, nullable=False)
    password = Column(String(length=255), nullable=False)
    email = Column(EmailType(length=255), unique=True, nullable=False)

    contact = relationship('Contact', back_populates='user')

    def __repr__(self):
        return f'<User {self.login}>'
