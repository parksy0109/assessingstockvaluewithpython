from src.main.stock.StockService import StockService
from src.main.stock.StockRepository import StockRepository
from src.main.stock.StockRepositoryImpl import StockRepositoryImpl
from src.main.stock.Stock import Stock
from src.main.dto.StockValuationDTO import StockValuationDTO
from src.main.utilitys.LogUtils import Log


class StockServiceImpl(StockService):
    stockRepository: StockRepository = StockRepositoryImpl()

    def getRatedStocksAtPERAverage(self, groupCode):
        Log.d("StockServiceImpl", "getRatedStocksAtPERAverage", groupCode)
        stockValuationDTOs: list[StockValuationDTO] = []
        stockPERs: list[float] = []

        stocks: list[Stock] = self.stockRepository.findStocksByGroupCode(groupCode)

        for stock in stocks:
            stockPERs.append(stock.priceEarningsRatio)

        averagePER = sum(stockPERs) / len(stockPERs)

        for stock in stocks:
            stockValuationDTOs.append(StockValuationDTO.transfer(stock, averagePER))

        return stockValuationDTOs
