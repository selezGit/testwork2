import uuid

from db import Base
from sqlalchemy import (VARCHAR, Column, Date, ForeignKey, String, Table,
                        UniqueConstraint)
from sqlalchemy.orm import backref, relationship
from sqlalchemy_utils import PhoneNumberType

user_phone_book = Table(
    'user_phone_book',
    Base.metadata,
    Column(
        'user_id',
        VARCHAR(length=36),
        ForeignKey('users.id'),
        primary_key=True,
    ),
    Column(
        'phone_book_id',
        VARCHAR(length=36),
        ForeignKey('phone_book.id'),
        primary_key=True,
    ),
    UniqueConstraint(
        'user_id',
        'phone_book_id',
        name='user_id_phone_book_id_together_uniq',
    ),
)


class PhoneBook(Base):
    __tablename__ = 'phone_book'
    __table_args__ = (
        UniqueConstraint(
            'first_name',
            'last_name',
            'phone_number',
            'birthday',
            name='name_phone_birthday_together_uniq',
        ),
        {'extend_existing': True},
    )

    id = Column(
        'id',
        VARCHAR(length=36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False,
    )
    first_name = Column(String(length=100), nullable=False)
    last_name = Column(String(length=100), nullable=False)
    phone_number = Column(PhoneNumberType(region='RU', max_length=12))

    birthday = Column(Date(), nullable=False)

    phone_book = relationship(
        'PhoneBook',
        secondary=user_phone_book,
        lazy='subquery',
        backref=backref('phone_book', lazy=True),
    )

    def __repr__(self):
        return f'<{self.last_name} {self.first_name}>'
