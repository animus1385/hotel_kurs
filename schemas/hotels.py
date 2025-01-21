from pydantic import BaseModel, Field


class Hotel(BaseModel):
    city:str
    contry:str
    name:str

class HotelPATCH(BaseModel):
    name:str | None = Field(None,description="Название отеля"),
    city:str | None  = Field(None,description="Город"),
    contry: str | None = Field(None,description="Название страны"),

