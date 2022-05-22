from pykrx import stock
import pandas as pd
from src.main.stock.StockServiceImpl import StockServiceImpl
from src.main.constants.GroupCodes import GroupCodes

# 테이블 설정 전체 보기
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

if __name__ == '__main__':

    impl = StockServiceImpl()

    stockValuationDTOs = impl.getRatedStocksAtPERAverage(GroupCodes.MACHINE)

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

