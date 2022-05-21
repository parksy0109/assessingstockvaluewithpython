from dataclasses import dataclass
from src.main.stock.Stock import Stock


@dataclass
class StockValuationDTO:
    name: str
    currentPrice: float
    priceEarningsRatio: float
    earningPerShare: float
    reasonableStockPrice: float
    evaluation: str

    # 생성자
    def __init__(self, name, currentPrice, priceEarningsRatio, earningPerShare, reasonableStockPrice, evaluation):
        self.name = name
        self.currentPrice = currentPrice
        self.priceEarningsRatio = priceEarningsRatio
        self.earningPerShare = earningPerShare
        self.reasonableStockPrice = reasonableStockPrice
        self.evaluation = evaluation

    @staticmethod
    def transfer(stock: Stock, averagePER):
        evaluation: str
        if stock.priceEarningsRatio == 0:
            evaluation = "측정불가"
        elif stock.priceEarningsRatio < averagePER:
            evaluation = "저평가"
        elif stock.priceEarningsRatio == averagePER:
            evaluation = "평균"
        else:
            evaluation = "고평가"

        return StockValuationDTO(
            stock.name,
            stock.currentPrice,
            round(stock.priceEarningsRatio, 3),
            round(stock.earningPerShare, 3),
            round(stock.earningPerShare * averagePER, 3),
            evaluation
        )
