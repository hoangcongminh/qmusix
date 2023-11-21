"""App custom response"""

from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class Status:
    is_error: bool
    code: int
    error_message: str
    alerta_message: str


@dataclass
class Response:
    status: Status
    data: Any

    @classmethod
    def Fail(cls, code: int, error_message: str, alerta_message: str, data: Any):
        status = Status(
            is_error=True,
            code=code,
            error_message=error_message,
            alerta_message=alerta_message,
        )
        return asdict(cls(status=status, data=data))

    @classmethod
    def OK(cls, data: Any):
        status = Status(
            is_error=False,
            code=None,
            error_message=None,
            alerta_message=None,
        )
        return asdict(cls(status=status, data=data))
