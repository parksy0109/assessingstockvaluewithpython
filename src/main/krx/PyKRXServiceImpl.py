from pykrx import stock
from src.main.krx.PyKRXService import PyKRXService
from src.main.stock.StockServiceImpl import StockServiceImpl


class PyKRXServiceImpl(PyKRXService):
    def getRatedStocksAtPERAverage(self, groupCode):
        # StockService 구현체 초기화
        stockService = StockServiceImpl()

        # 그룹코드로 주식 이름 가져와 DTO 로 변환하여 넣어준다
        # return : list[StockValuationDTO]
        stockValuationDTOs = stockService.getRatedStocksAtPERAverage(groupCode)

        # StockCodes 초기화
        stockCodes: list[str] = []

        for stockValuationDTO in stockValuationDTOs:
            stockCodes.append(stockValuationDTO.name)

        for i in range(0, len(stockCodes)):
            # StartDate , EndDate, StockCode
            startDate = '20220101'
            endDate = '20220522'
            stockCode = stockCodes[i]
            df = stock.get_market_fundamental(startDate, endDate, stockCode, freq='d', name_display=True)

            values = df.columns.values
            perList = df['PER'].tolist()
            pbrList = df['PBR'].tolist()

            ticker_list = stock.get_market_ticker_list()

            stockName: str

            print(stock.get_market_ticker_name(stockCode))
            print(startDate + " 부터 " + endDate + " 까지 평균 PER :: " + round((sum(perList) / len(perList)), 2).__str__())

            print(startDate + " 부터 " + endDate + " 까지 평균 PBR :: " + round((sum(pbrList) / len(pbrList)), 2).__str__(),
                  end="\n\n")

            print(endDate + " PER :: " + str(round(perList[-1], 2)))
            print(endDate + " PBR :: " + str(round(pbrList[-1], 2)), end="\n\n")
