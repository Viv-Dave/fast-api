from fastapi import FastAPI 
from app.routes.notes import router 
app = FastAPI()

app.include_router(router)
# @app.get("/")
# async def greetings():
#     return {"Welcome to the Notes app"}