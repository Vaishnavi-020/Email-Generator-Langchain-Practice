from pydantic import BaseModel

class EmailOut(BaseModel):
    subject:str
    greeting:str
    body:str
    closing:str
    