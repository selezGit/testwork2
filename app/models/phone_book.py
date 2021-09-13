import uuid

from db import Base
from sqlalchemy import VARCHAR, Column, Date, ForeignKey, String, UniqueConstraint
from sqlalchemy_utils import PhoneNumberType


class PhoneBook(Base):
    __tablename__ = 'phone_book'
    __table_args__ = (
        UniqueConstraint(
            'user_id',
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
    user_id = Column('user_id', VARCHAR(length=36), ForeignKey('users.id'))
    first_name = Column(String(length=100), nullable=False)
    last_name = Column(String(length=100), nullable=False)
    phone_number = Column(PhoneNumberType(region='RU', max_length=12))
    birthday = Column(Date(), nullable=False)

    def __repr__(self):
        return f'<{self.last_name} {self.first_name}>'
