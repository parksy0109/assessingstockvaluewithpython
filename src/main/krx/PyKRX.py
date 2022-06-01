from dataclasses import dataclass


@dataclass
class PyKRX:
    date: str
    BPS: int
    PER: float
    PBR: float
    EPS: int
    DIV: float
    DPS: int
