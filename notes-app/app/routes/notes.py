from fastapi import APIRouter, Query
from typing import Annotated
from app.schema.notes import Note
from enum import Enum 
router = APIRouter(prefix="/notes", tags=["notes"])
class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"    
notes_list = [];
@router.get("/")
async def greetings():
    return {"Welcome to the Notes app"}

@router.get("/list_notes")
async def get_notes(
    priority: Annotated[str | None, Query()] = None
):

    if priority is None:
        return {"notes": notes_list}

    filtered_notes = [
        note for note in notes_list
        if note["note_priority"] == priority
    ]

    return {"notes": filtered_notes}

@router.get("/search_note")
async def search_note(
    title: Annotated[str | None, Query()] = None, 
    id: Annotated[str | None, Query()] = None
):
    return notes_list;

@router.post("/create_note")
async def create_note(note: Note):
    note.note_id = len(notes_list)+1
    notes_list.append(note.dict())
    return {
        "message": "Note created",
        "note": note
    }