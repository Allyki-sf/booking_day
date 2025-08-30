
from fastapi import APIRouter, HTTPException
from app.data import all_data
from app.base import DataRequest


router = APIRouter(prefix="/date")


@router.get("/all_free_days")
async def free_month():

    free_list = [key for key, value in all_data.items() if value]

    return {"message": f"{str(free_list)} is free"}


@router.put("/get_date")
async def get_date(request: DataRequest):
    date = request.date

    if date not in all_data:
        raise HTTPException(status_code=404, detail="date not found")

    if not all_data[date]:
        return {"message": f"{date} is not free"}

    all_data[date] = False
    return {"message": f"{date} is booked"}


@router.put("/cancel_date")
async def cancel_date(request: DataRequest):
    date = request.date

    if date > 31:
        raise HTTPException(status_code=404, detail="date not found")

    if all_data[date]:
        return {"message": f"{date} is already free"}

    all_data[date] = True
    return {"message": f"{date} is canceled"}

