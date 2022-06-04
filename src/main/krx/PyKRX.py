from dataclasses import dataclass


@dataclass
class PyKRX:
    date: str
    currentPrice: float
    BPS: int
    PER: float
    PBR: float
    EPS: int
    DIV: float
    DPS: int
