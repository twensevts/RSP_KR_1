from pydantic import BaseModel, field_validator
from annotated_types import Len
from typing import Annotated


class User(BaseModel):
    name: str
    age: int


FORBIDDEN_WORDS = ["кринж", "рофл", "вайб"]


class Feedback(BaseModel):
    name: Annotated[str, Len(min_length=2, max_length=50)]
    message: Annotated[str, Len(min_length=10, max_length=500)]

    @field_validator("message")
    @classmethod
    def check_forbidden_words(cls, v: str) -> str:
        text = v.lower()
        for word in FORBIDDEN_WORDS:
            if word in text:
                raise ValueError("Использование недопустимых слов")
        return v
