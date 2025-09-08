from pydantic import BaseModel

class DataRequest(BaseModel):
    day: int


class DataResponse(DataRequest):
    status: str

    class Config:
        from_attributes = True