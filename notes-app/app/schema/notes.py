from pydantic import BaseModel
from app.routes.notes import Priority
class Note(BaseModel):
    note_id: int = 0
    note_priority: Priority
    title: str
    description: str