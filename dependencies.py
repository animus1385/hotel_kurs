from typing import Annotated
from fastapi import Depends, Query
from pydantic import BaseModel

class PaginationParams(BaseModel):
    page: Annotated[int | None, Query(None,description="Номер страницы",gt=1,)]
    per_page: Annotated[int | None, Query(None,description="Кол-во элементов",gt=1,lt=3)]
    
    
PaginationDep = Annotated[PaginationParams,Depends]