from pydantic import BaseModel

"""
orm_mode = True
DoneResponse implicitly receive an ORM and convert it to a response schema.
FYI:
https://zenn.dev/sh0nk/books/537bb028709ab9/viewer/b92ab0
"""


class DoneResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True
