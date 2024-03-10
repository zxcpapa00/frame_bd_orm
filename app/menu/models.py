import uuid

from sqlalchemy import Column, String, Uuid
from sqlalchemy.orm import relationship

from app.database import Base


class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True)
    description = Column(String)
    submenus = relationship('SubMenu', back_populates='menu', cascade='all, delete', lazy='selectin')

    def __str__(self):
        return f'Menu: {self.title}'
