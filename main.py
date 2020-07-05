from fastapi import FastAPI
from fastapi import HTTPException
from db import PhraseInput
from db import PhraseOutput
from db import Database

app = FastAPI(title="Random phrase")
db = Database()

@app.get(
    "/get",
    response_description = "Random_phrase",
    description = "Get random phrase from database",
    response_model = PhraseOutput,
)

async def get():
    try:
        phrase = db.get(db.get_random())
    except IndexError:
        raise HTTPException(404, "Phrase list is empty")
    return phrase


@app.post(
    "/add",
    response_description="Added phrase with *id* parameter",
    response_model=PhraseOutput,
)
async def add(phrase: PhraseInput):
    phrase_out = db.add(phrase)
    return phrase_out


@app.delete("/delete", response_description="Result of deleting")
async def delete(id: int):
    try:
        db.delete(id)
    except ValueError as e:
        raise HTTPException(404, str(e))
