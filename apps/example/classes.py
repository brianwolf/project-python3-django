from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Example:
    string: str
    integer: int
    decimal: float
    id: Optional[int] = None
    date: datetime = field(default=datetime.now())

    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id
