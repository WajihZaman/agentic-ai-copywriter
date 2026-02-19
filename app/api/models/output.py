from pydantic import BaseModel


class Reply(BaseModel):
    Title: str
    Response: str
    sources: list[str]
    tools_used: list[str]
