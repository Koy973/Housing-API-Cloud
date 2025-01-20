# app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal, engine

# Créer les tables si elles n'existent pas déjà
# (Normalement, on utilise Alembic, mais ceci peut servir de fallback)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dépendance pour avoir une session par requête
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/houses", response_model=list[schemas.HouseOut])
def get_houses(db: Session = Depends(get_db)):
    houses = db.query(models.House).all()
    return houses

@app.post("/houses", response_model=schemas.HouseOut)
def create_house(house: schemas.HouseCreate, db: Session = Depends(get_db)):
    new_house = models.House(**house.dict())
    db.add(new_house)
    db.commit()
    db.refresh(new_house)
    return new_house

