from pydantic import BaseModel

class PolymerInput(BaseModel):
    structure: str
    additives: list[str]
    temperature: float
