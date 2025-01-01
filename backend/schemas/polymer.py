from pydantic import BaseModel, Field
from typing import List

class PolymerInput(BaseModel):
    structure: str = Field(..., description="The structure of the polymer, represented as a string.")
    additives: List[str] = Field(..., description="A list of additives used in the polymer.")
    temperature: float = Field(..., description="The temperature at which the polymer operates.")

    def __str__(self) -> str:
        return (
            f"PolymerInput(structure={self.structure}, "
            f"additives={self.additives}, "
            f"temperature={self.temperature})"
        )
