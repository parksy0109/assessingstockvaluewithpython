from dataclasses import dataclass
from src.main.stock.Stock import Stock


@dataclass
class StockValuationDTO:
    name: str
    code: str
    currentPrice: float
    priceEarningsRatio: float
    earningPerShare: float
    returnOnEquity: float
    reasonableStockPrice: float
    evaluation: str

    # 생성자
    def __init__(self, name, code, currentPrice, priceEarningsRatio, earningPerShare, returnOnEquity,
                 reasonableStockPrice, evaluation):
        self.name = name
        self.code = code
        self.currentPrice = currentPrice
        self.priceEarningsRatio = priceEarningsRatio
        self.earningPerShare = earningPerShare
        self.returnOnEquity = returnOnEquity
        self.reasonableStockPrice = reasonableStockPrice
        self.evaluation = evaluation

    @staticmethod
    def transfer(stock: Stock, averagePER):
        evaluation: str
        per = stock.earningPerShare * averagePER
        if stock.currentPrice > per:
            evaluation = "☆"
        elif stock.currentPrice == per:
            evaluation = "="
        else:
            evaluation = "★"

        return StockValuationDTO(
            stock.name,
            stock.code,
            stock.currentPrice,
            round(stock.priceEarningsRatio, 2),
            round(stock.earningPerShare, 2),
            round(stock.returnOnEquity, 2),
            round(stock.earningPerShare * averagePER, 2),
            evaluation
        )
