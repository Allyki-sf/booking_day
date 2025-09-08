
from fastapi import APIRouter, Path, HTTPException
from fastapi.params import Depends
from fastapi.responses import HTMLResponse

from sqlalchemy.ext.asyncio import AsyncSession

from typing import Annotated

from app.data import all_data
from app.schemas import DataRequest
from app.time_helper import year, month_name, days_in_month
from core.models import crud, db_helper


router = APIRouter(prefix="/date")


@router.get("/all_days",
            response_class=HTMLResponse
            )
async def all_month(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    all_days = await crud.get_all_days(session=session)
    html = "<br>".join([f"Day {day.day}: {day.status}" for day in all_days])
    return f"<html><body><h2>{month_name} {year}</h2>{html}</body></html>"


@router.get("/all_free_days",
            response_class=HTMLResponse
            )
async def free_month(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    free_days = await crud.get_free_days(session=session)
    html = "<br>".join([f"Day {day.day}: {day.status}" for day in free_days])
    return f"<html><body><h2>{month_name} {year}</h2>{html}</body></html>"


#@router.get("/all_free_days")
#async def free_month():

#    free_list = [key for key, value in all_data.items() if value]

#    free_list = [f"[{now_day()}]" if key == now_day() else key for key in free_list]

#    return {"message": f"{free_list} is free"}

@router.get("/booked_day/{day}")
async def booking_day(
        day: Annotated[int, Path(ge=1, lt=days_in_month+1)],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.take_free_day(
        session=session,
        day=day,
    )

#@router.put("/get_date")
#async def get_date(request: DataRequest):
#    date = request.date

#    if date not in all_data:
#        raise HTTPException(status_code=404, detail="date not found")

#    if not all_data[date]:
#        return {"message": f"{date} is not free"}

#    all_data[date] = False
#   return {"message": f"{date} is booked"}


@router.put("/cancel_date")
async def cancel_date(request: DataRequest):
    date = request.date

    if date > 31 or date <= 0:
        raise HTTPException(status_code=404, detail="date not found")

    if all_data[date]:
        return {"message": f"{date} is already free"}

    all_data[date] = True
    return {"message": f"{date} is canceled"}

