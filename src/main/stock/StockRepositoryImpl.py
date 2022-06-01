import win32com.client
from src.main.stock.StockRepository import StockRepository
from src.main.utilitys.LogUtils import Log
from src.main.stock.Stock import Stock


class StockRepositoryImpl(StockRepository):
    # 대신 증권 API 오브젝트 가져오기
    instCpCybos = win32com.client.Dispatch('CpUtil.CpCybos')
    instCpStockCode = win32com.client.Dispatch('CpUtil.CpStockCode')
    instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")
    instCpCodMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")

    def findStockCodeByStockName(self, stockName):
        return stockName

    # 종목 코드를 파라미터로 받아 주식 객체 리턴하는 메소드
    def findByStockCode(self, stockCode):
        Log.d("StockRepositoryImpl", "findByStockCode", stockCode)

        # instMarketEye Setting
        # 4 - 현재가, 67 - PER, 70 - EPS, 107 - 분기 ROE, 111 - 최근분기년월
        self.instMarketEye.SetInputValue(0, (4, 67, 70, 107, 111))
        self.instMarketEye.SetInputValue(1, stockCode)
        self.instMarketEye.BlockRequest()

        # 조회를 통해 나온 데이터 Stock Object 로 만들어 리턴
        return Stock(self.instCpStockCode.GetData(1, self.instCpStockCode.CodeToIndex(stockCode)),
                     stockCode[1:],
                     self.instMarketEye.GetDataValue(0, 0),
                     self.instMarketEye.GetDataValue(1, 0),
                     self.instMarketEye.GetDataValue(2, 0),
                     self.instMarketEye.GetDataValue(3, 0))

    # 그룹 코드를 파라미터로 받아 해당 그룹의 종목 코드 리스트를 반환하는 메소드
    def findStockCodesByGroupCode(self, groupCode):
        Log.d("StockRepositoryImpl", "findStockCodesByGroupCode", groupCode)
        return self.instCpCodMgr.GetGroupCodeList(groupCode)

    def findStocksByGroupCode(self, groupCode):
        Log.d("StockRepositoryImpl", "findStocksByGroupCode", groupCode)
        stocks: list[Stock] = []
        stockCodes = self.findStockCodesByGroupCode(groupCode)
        for stockCode in stockCodes:
            if self.findByStockCode(stockCode).priceEarningsRatio != 0:
                stocks.append(self.findByStockCode(stockCode))
        return stocks
