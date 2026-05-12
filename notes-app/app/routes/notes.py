from fastapi import APIRouter

router = APIRouter(prefix="/notes", tags=["notes"])

@router.get("/")
async def greetings():
    return {"Welcome to the Notes app"}