import uuid
from sqlalchemy import String, ForeignKey, Column, Uuid
from sqlalchemy.orm import relationship

from app.database import Base


class SubMenu(Base):
    __tablename__ = "submenu"

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True)
    description = Column(String)
    menu_id = Column(Uuid, ForeignKey('menu.id', ondelete='CASCADE'))
    menu = relationship('Menu', back_populates='submenus', cascade='all', lazy='selectin')
    dishes = relationship('Dish', back_populates='submenu', cascade='all', lazy='selectin')
