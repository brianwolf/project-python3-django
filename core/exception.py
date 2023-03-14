from dataclasses import dataclass
from enum import Enum
from typing import Dict


@dataclass
class AppException(Exception):
    code: Enum
    msj: str = None
    exception: Exception = None

    def to_json(self) -> Dict[str, object]:
        d = {'code': self.code.value, 'msj': self.msj}
        if self.exception:
            d['exception'] = str(self.exception)
        return d
