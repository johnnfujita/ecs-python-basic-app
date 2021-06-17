from pydantic import BaseModel
from typing import List, Optional 


class _UserLogin(BaseModel):
    username: str
    password: str
    class Config():
        orm_mode = True

class ShowItem(BaseModel):
    title: str
    description: str
    class Config():
        orm_mode =True


class _User(BaseModel):
    name: str
    email: str
    password: str
    

class _UserShow(BaseModel):
    name: str
    email: str
    items: List[ShowItem] = []
    class Config():
        orm_mode =True
class User_Little(BaseModel):
    name: str
    class Config():
        orm_mode =True

class Item(BaseModel):
    title: str
    description: str
    creator: User_Little
    class Config():
        orm_mode =True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None