from typing import Optional

from pydantic import BaseModel


class CodeRunPayloadFile(BaseModel):
    name: str
    content: str


class CodeRunPayload(BaseModel):
    language: str
    command: Optional[str]
    files: list[CodeRunPayloadFile]


class CodeRun(BaseModel):
    image: str
    payload: CodeRunPayload
