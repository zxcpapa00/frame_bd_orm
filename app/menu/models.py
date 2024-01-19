from sqlalchemy import Integer, String, ForeignKey, Column

from app.database import Base


class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    submenu_id = Column(ForeignKey("submenu.id"))
