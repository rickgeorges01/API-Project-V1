from sqlalchemy.orm import Session
from . import models, params

def create_dict(dictionary :params.PostDictParams, db: Session ):
    #creation d'un nouveau dictionnaire
    new_dict = models.Dictionary(name = dictionary.name)
    db.add(new_dict)
    db.commit()
    db.refresh(new_dict)

    for line in dictionary.lines :
        new_line = models.DictionaryLines(letter = line.letter, conv = line.conv, dict_id = new_dict.id)
        db.add (new_line)
    db.commit()

    return new_dict

def update_dict(dict_id: int, new_data: params.PostDictParams, db: Session):
    dict_to_update = db.query(models.Dictionary).filter(models.Dictionary.id == dict_id).first()

    if dict_to_update is None:
        return None  # Ou gérer l'erreur selon vos besoins

    # Mise à jour des informations du dictionnaire
    dict_to_update.name = new_data.name
    db.commit()

    # Supprimer les anciennes lignes et ajouter les nouvelles
    db.query(models.DictionaryLines).filter(models.DictionaryLines.dict_id == dict_id).delete()
    for line in new_data.lines:
        new_line = models.DictionaryLines(letter=line.letter, conv=line.conv, dict_id=dict_id)
        db.add(new_line)
    db.commit()

    return dict_to_update

def delete_dict(dict_id: int, db: Session):
    # Trouver le dictionnaire par id
    dict_to_delete = db.query(models.Dictionary).filter(models.Dictionary.id == dict_id).first()

    # Vérifier si le dictionnaire existe
    if dict_to_delete is None:
        return None  # Ou gérer l'erreur comme vous le souhaitez

    # Supprimer les lignes associées (si nécessaire)
    db.query(models.DictionaryLines).filter(models.DictionaryLines.dict_id == dict_id).delete()

    # Supprimer le dictionnaire
    db.delete(dict_to_delete)
    db.commit()

    return dict_to_delete 


def read_dict(dict_id: int, db: Session):
    # Rechercher le dictionnaire par son id
    dict = db.query(models.Dictionary).filter(models.Dictionary.id == dict_id).first()

    # Vérifier si le dictionnaire existe
    if dict is None:
        return None  # Ou gérer l'erreur selon vos besoins

    return dict

def translate_word(word: str, dictionary_name: str, db: Session):
    # Recherche du dictionnaire spécifique
    dictionary = db.query(models.Dictionary).filter(models.Dictionary.name == dictionary_name).first()
    if not dictionary:
        return "Dictionnaire non trouvé"

    # Traduction lettre par lettre
    translated_word = ""
    for letter in word:
        # Recherche de la traduction de chaque lettre dans les lignes du dictionnaire
        translation = db.query(models.DictionaryLines).filter(
            models.DictionaryLines.dict_id == dictionary.id,
            models.DictionaryLines.letter == letter
        ).first()

        if translation:
            translated_word += translation.conv
        else:
            # Si aucune correspondance n'est trouvée, utilisez la lettre originale
            translated_word += letter

    return translated_word


def create_translation(word: str, translation: str, dictionary_name: str, db: Session):
    new_translation = models.Trad(word=word, trad=translation, dictionnary=dictionary_name)
    db.add(new_translation)
    db.commit()
    db.refresh(new_translation)
    return new_translation



