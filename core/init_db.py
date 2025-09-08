from sqlalchemy import select
from core.models import Base, Month, db_helper
from app.time_helper import days_in_month


async def init_db():
    async with db_helper.engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    async with db_helper.session_factory() as session:
        result = await session.execute(
            select(Month).limit(1)
        )
        exists = result.scalar_one_or_none()
        if not exists:
            session.add_all([
                Month(day=i, status="Free")
                for i in range(1, days_in_month + 1)
                ])
            await session.commit()