from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession



from fastapi import HTTPException

from .month import Month
from app.time_helper import days_in_month


async def get_all_days(session: AsyncSession) -> list[Month]:
    stmt = select(Month).order_by(Month.day)
    result: Result = await session.execute(stmt)
    all_days = result.scalars().all()
    return list(all_days)


async def get_free_days(session: AsyncSession) -> list[Month]:
    stmt = select(Month).where(Month.status == "Free").order_by(Month.day)
    result: Result = await session.execute(stmt)
    free_days = result.scalars().all()
    return list(free_days)


async def take_free_day(
        session: AsyncSession,
        day: int
):
    stmt = select(Month).where(Month.day == day,Month.status == "Free")
    result = await session.execute(stmt)
    free_day = result.scalars().first()

    if not free_day :
        raise HTTPException(status_code=400, detail="Day is already booked or does not exist")

    free_day.status = "Booked"

    await session.commit()
    return {"message": f"Day {day} successfully booked"}

