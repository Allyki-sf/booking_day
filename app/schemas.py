from typing import Annotated

from fastapi import Path
from pydantic import BaseModel

from app.time_helper import days_in_month


class DataRequest(BaseModel):
    day: Annotated[int, Path(ge=1, lt=days_in_month+1)]


class DataResponse(DataRequest):
    status: str

    class Config:
        from_attributes = True