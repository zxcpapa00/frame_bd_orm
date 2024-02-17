from sqlalchemy import select, insert, delete, update, func
from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: str):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(id=model_id)
            result = await session.execute(query)
            return result.mappings().one_or_none()

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
    async def delete_by_id(cls, model_id: str):
        async with async_session_maker() as session:
            query = delete(cls.model.__table__).where(cls.model.__table__.c.id == model_id)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update_by_id(cls, model_id: str, **data):
        async with async_session_maker() as session:
            query = update(cls.model.__table__).where(cls.model.__table__.c.id == model_id).values(**data)
            await session.execute(query)
            await session.commit()

            query = select(cls.model).filter_by(**data)
            result = await session.execute(query)
            added_object = result.scalar()  # Получаем объект из результата запроса
            return added_object
