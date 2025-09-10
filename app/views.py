
from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.responses import HTMLResponse

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import DataRequest
from app.time_helper import year, month_name
from core.models import crud, db_helper


router = APIRouter(prefix="/date")


@router.get("/all_days",
            response_class=HTMLResponse
            )
async def all_month(
        session: AsyncSession = Depends(db_helper.session_dependency),
):
    all_days = await crud.get_all_days(session=session)
    html = "<br>".join([f"Day {day.day}: {day.status}" for day in all_days])
    return f"<html><body><h2>{month_name} {year}</h2>{html}</body></html>"


@router.get("/all_free_days",
            response_class=HTMLResponse
            )
async def free_month(
        session: AsyncSession = Depends(db_helper.session_dependency),
):
    free_days = await crud.get_free_days(session=session)
    html = "<br>".join([f"Day {day.day}: {day.status}" for day in free_days])
    return f"<html><body><h2>{month_name} {year}</h2>{html}</body></html>"


@router.post("/booked_day/{day}")
async def booking_day(
        data: DataRequest,
        session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.take_free_day(
        session=session,
        day=data.day,
    )


@router.delete("/cancel_booking/{day}")
async def cancel_booking_day(
        data: DataRequest,
        session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.cancel_booking(
        session=session,
        day=data.day,
    )

