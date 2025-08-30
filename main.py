from fastapi import FastAPI
import uvicorn

from app import posts


app = FastAPI()


app.include_router(posts.router)


@app.get("/")
async def root():
    return {"message": "Hello API"}



# class Hotel:
#     def __init__(self, first_date, last_date):
#         self.first_date = first_date
#         self.last_date = last_date


# class Rooms:
#     def __init__(self, number, first_date, last_date):
#         self.number = number
#         self.first_date = first_date
#         self.last_date = last_date




if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)