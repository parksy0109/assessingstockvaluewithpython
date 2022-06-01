from pykrx import stock
from src.main.krx.PyKRXService import PyKRXService
from src.main.krx.PyKRX import PyKRX
import pandas as pd

# # 테이블 설정 전체 보기
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


class PyKRXServiceImpl(PyKRXService):
    def getStockDataByPeriod(self, stockCode):
        # StartDate , EndDate, StockCode
        startDate = '20220101'
        endDate = '20220602'
        df = stock.get_market_fundamental(startDate, endDate, stockCode, freq='d', name_display=True)

        dateIndex = df.index.values
        values = df.columns.values

        bpsList = df['BPS'].tolist()
        perList = df['PER'].tolist()
        pbrList = df['PBR'].tolist()
        epsList = df['EPS'].tolist()
        divList = df['DIV'].tolist()
        dpsList = df['DPS'].tolist()

        result: list[PyKRX] = []

        for i in range(0, len(bpsList)):
            result.append(PyKRX(str(dateIndex[i])[0:11],
                                bpsList[i],
                                perList[i],
                                round(pbrList[i], 2),
                                epsList[i],
                                round(divList[i], 2),
                                dpsList[i]))

        return result


if __name__ == '__main__':
    impl = PyKRXServiceImpl()
    period = impl.getStockDataByPeriod("000990")
    print(period)
