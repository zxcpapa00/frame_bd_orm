from sqlalchemy import Integer, String, ForeignKey, Column

from app.database import Base


class SubMenu(Base):
    __tablename__ = "submenu"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
