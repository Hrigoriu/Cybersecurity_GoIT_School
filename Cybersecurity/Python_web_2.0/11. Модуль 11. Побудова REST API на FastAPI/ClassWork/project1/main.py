from db import Note, get_db
from fastapi import Depends, FastAPI, HTTPException, Path,  status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

app = FastAPI()


class ResponseNoteModel(BaseModel):
    id: int = Field(default=1, ge=1)
    name: str
    description: str
    done: bool


@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    try:
        # Здійснюємо запит
        result = db.execute("SELECT 1").fetchone()
        if result is None:  # noqa: F821
            raise HTTPException(
                status_code=500, detail="Database is not configured correctly"
            )
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")



@app.get("/notes/{note_id}", response_model=ResponseNoteModel)
async def read_note(
    note_id: int = Path(description="The ID of the note to get", gt=0, le=10),
    db: Session = Depends(get_db),
):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return note


class NoteModel(BaseModel):
    name: str
    description: str
    done: bool


@app.post("/notes")
async def create_note(note: NoteModel, db: Session = Depends(get_db)):
    new_note = Note(name=note.name, description=note.description, done=note.done)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)


#return new_note


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = {"item_id": item_id, "name": "Foo"}
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
