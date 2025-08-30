from pydantic import BaseModel

class DataRequest(BaseModel):
    date: int