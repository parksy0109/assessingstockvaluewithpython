from dataclasses import dataclass


@dataclass
class Stock:
    name: str
    code: str
    currentPrice: float
    priceEarningsRatio: float
    earningPerShare: float
    returnOnEquity: float

    # 생성자
    def __init__(self, name, code, currentPrice, priceEarningsRatio, earningPerShare, returnOnEquity):
        self.name = name
        self.code = code
        self.currentPrice = currentPrice
        self.priceEarningsRatio = priceEarningsRatio
        self.earningPerShare = earningPerShare
        self.returnOnEquity = returnOnEquity
