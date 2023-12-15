from fastapi import FastAPI, Depends
from .params import PostTradParams, PostDictParams
from .reponses import PostTradResponse, GetTradResponse, PostDictionary
from .models import Base,Trad
from .database import engine,SessionLocal
from sqlalchemy.orm import Session
from . import crud

#Création des tables dans la bd
Base.metadata.create_all(bind = engine)
app = FastAPI()

#Fonction pour obtenir la session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/TranslateDict", response_model=GetTradResponse)
def traduire_mot(params: PostTradParams, db: Session = Depends(get_db)):
    traduction = crud.translate_word(params.word, params.dictionnary, db)
    if traduction == "Dictionnaire non trouvé":
        raise HTTPException(status_code=404, detail="Dictionnaire non trouvé")
    return {"word": params.word, "trad": traduction}


@app.post("/CreateDict", response_model = PostDictionary)
def create_dict(params : PostDictParams, db: Session = Depends(get_db) ):
    #creation d'un nouveau dictionnaire
   return crud.create_dict(params, db)

@app.get("/ReadDict/{dict_id}", response_model=PostDictionary)
def get_dict(dict_id: int, db: Session = Depends(get_db)):
    db_dict = crud.read_dict(dict_id, db)
    if db_dict is None:
        raise HTTPException(status_code=404, detail="Dictionnaire non trouvé")
    return db_dict

@app.put("/UpdateDict/{dict_id}", response_model=PostDictionary)
def update_dict(dict_id: int, dict_params:PostDictParams, db: Session = Depends(get_db)):
    updated_dict = crud.update_dict(dict_id, dict_params, db)
    if updated_dict is None:
        raise HTTPException(status_code=404, detail="Dictionnaire non trouvé pour mise à jour")
    return updated_dict
    
@app.delete("/DeleteDict/{dict_id}", response_model=PostDictionary)
def delete_dictionary(dict_id: int, db: Session = Depends(get_db)):
    deleted_dict = crud.delete_dict(dict_id, db)
    if deleted_dict is None:
        raise HTTPException(status_code=404, detail="Dictionnaire non trouvé")
    return deleted_dict


async def create_item(item: GetTradResponse, db: Session = Depends(get_db)):
    db_item = Trad(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
