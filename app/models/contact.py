import uuid

from db import Model
from sqlalchemy import VARCHAR, Column, Date, ForeignKey, String, UniqueConstraint
from sqlalchemy_utils import PhoneNumberType
from sqlalchemy.orm import relationship


class Contact(Model):
    __tablename__ = 'contacts'
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
    user_id = Column('user_id', VARCHAR(length=36), ForeignKey('users.id'), nullable=False)
    first_name = Column(String(length=100), nullable=False)
    last_name = Column(String(length=100), nullable=False)
    phone_number = Column(PhoneNumberType(region='RU', max_length=12), nullable=False)
    birthday = Column(Date(), nullable=False)

    user = relationship('User', back_populates='contact')

    def __repr__(self):
        return f'<Contact {self.last_name} {self.first_name}>'
