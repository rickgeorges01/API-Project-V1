from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


from .database import Base

#Création de la table qui stockera les traductions
class Trad(Base):
    __tablename__ = "trads"

    id = Column(Integer, primary_key=True, index=True)
    trad = Column(String(255))
    word = Column(String(40))
    dictionnary = Column(String(40))
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())

#Création de la table qui contient le type de dictionnaire 
class Dictionary(Base):
    __tablename__ = "dict"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40))

    #relation entre la table dict et dict_line 
    lines = relationship("DictionaryLines", back_populates="dict")

#Création de la table qui contient les traductions de chaque lettre 
class DictionaryLines(Base):
    __tablename__ = "dict_line"

    id = Column(Integer, primary_key=True, index=True)
    letter = Column(String(3))
    conv = Column(String(5))
    dict_id = Column(Integer, ForeignKey("dict.id"))

    dict = relationship("Dictionary", back_populates="lines")

