from pydantic import BaseModel

class GetTradResponse(BaseModel) :
    word : str
    trad : str

class PostTradResponse(BaseModel) :
    word : str
    dictionnary : str
    trad : str

class PostDictionaryLines(BaseModel) :
    id : int
    letter : str
    conv   : str 
    
    class config :
        orm_mode : True

class PostDictionary(BaseModel) :
    id : int
    name : str 
    lines : list[PostDictionaryLines] = []

    class config :
        orm_mode : True

    
    
