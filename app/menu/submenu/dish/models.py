from sqlalchemy import String, ForeignKey, Column, Uuid, Float
from sqlalchemy.orm import relationship

from app.database import Base
import uuid


class Dish(Base):
    __tablename__ = "dish"

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    submenu_id = Column(Uuid, ForeignKey('submenu.id', ondelete='CASCADE'))
    submenu = relationship('SubMenu', back_populates='dishes')
