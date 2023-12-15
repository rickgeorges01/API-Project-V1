from pydantic import BaseModel

class PostTradParams(BaseModel) :
    word: str
    dictionnary:str

class PostDictLines(BaseModel):
    letter : str
    conv : str

class PostDictParams(BaseModel):
    name : str  
    lines : list[PostDictLines] = []
    