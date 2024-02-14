import uuid

from sqlalchemy import select, insert, delete, update, func

from app.database import async_session_maker
from app.menu.models import Menu


class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id):
        async with async_session_maker() as session:
            try:
                query = select(cls.model.__table__.columns).filter_by(id=model_id)
                result = await session.execute(query)
                return result.mappings().all()
            except Exception as e:
                return None

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

        query = select(cls.model).filter_by(**data)
        result = await session.execute(query)
        added_object = result.scalar()  # Получаем объект из результата запроса
        return added_object

    @classmethod
    async def delete_by_id(cls, model_id: uuid.UUID):
        async with async_session_maker() as session:
            query = delete(Menu).filter_by(id=model_id)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update_by_id(cls, model_id: uuid.UUID, **data):
        async with async_session_maker() as session:
            query = update(Menu).values(**data).filter_by(id=model_id)
            await session.execute(query)
            await session.commit()
