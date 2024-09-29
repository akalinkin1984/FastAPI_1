import datetime
from typing import Literal

from pydantic import BaseModel


class IdReturnBase(BaseModel):
    id: int


class StatusSuccessBase(BaseModel):
    status: Literal["success"]


class GetAdvResponse(BaseModel):

    id: int
    title: str
    description: str
    price: float
    author: str
    create_date: datetime.datetime


class CreateAdvRequest(BaseModel):

    title: str
    description: str
    price: float
    author: str


class CreateAdvResponse(IdReturnBase):
    pass


class UpdateAdvRequest(BaseModel):

    title: str | None = None
    description: str | None = None
    price: float | None = None


class UpdateAdvResponse(IdReturnBase):
    pass


class DeleteAdvResponse(StatusSuccessBase):
    pass


class SearchAdvRequest(BaseModel):

    pass
