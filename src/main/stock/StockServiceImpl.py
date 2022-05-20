from src.main.stock.StockService import StockService
from src.main.stock.StockRepository import StockRepository
from src.main.stock.StockRepositoryImpl import StockRepositoryImpl
from src.main.stock.Stock import Stock
from src.main.dto.StockValuationDTO import StockValuationDTO


class StockServiceImpl(StockService):
    stockRepository: StockRepository = StockRepositoryImpl()

    def rateStocksAtPERAverage(self, groupCode) -> list[StockValuationDTO]:
        stockValuationDTOs: list[StockValuationDTO] = []
        stockPERs: list[float] = []

        stocks: list[Stock] = self.stockRepository.findStocksByGroupCode(groupCode)

        for stock in stocks:
            stockPERs.append(stock.priceEarningsRatio)

        averagePER = sum(stockPERs) / len(stockPERs)

        for stock in stocks:
            stockValuationDTOs.append(StockValuationDTO.transfer(stock, averagePER))

        return stockValuationDTOs
