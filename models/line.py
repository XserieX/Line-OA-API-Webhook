from typing import List, Optional
from pydantic import BaseModel

class Line(BaseModel):
    destination: str
    events: List[Optional[None]]