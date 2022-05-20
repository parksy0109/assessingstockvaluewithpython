from dataclasses import dataclass


@dataclass
class Stock:
    name: str
    currentPrice: float
    priceEarningsRatio: float
    earningPerShare: float

    # 생성자
    def __init__(self, name, currentPrice, priceEarningsRatio, earningPerShare):
        self.name = name
        self.currentPrice = currentPrice
        self.priceEarningsRatio = priceEarningsRatio
        self.earningPerShare = earningPerShare
