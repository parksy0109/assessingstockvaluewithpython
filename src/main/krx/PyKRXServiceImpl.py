from pykrx import stock
from src.main.krx.PyKRXService import PyKRXService
from src.main.krx.PyKRX import PyKRX
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# # # 테이블 설정 전체 보기
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)


class PyKRXServiceImpl(PyKRXService):
    def predict(self, stockCode):
        # StartDate , EndDate, StockCode
        startDate = '20210101'
        startDate2 = '20201202'
        endDate = '20220603'
        endDate2 = '20220504'
        df1 = stock.get_market_fundamental(startDate2, endDate2, stockCode, freq='d', name_display=True)
        df2 = stock.get_market_ohlcv(startDate, endDate, stockCode)

        df3 = stock.get_market_fundamental('2022-04-29', '2022-06-03', stockCode, freq='d', name_display=True)

        print(df1)
        print(df2)
        print(df3)

        # perList = df1['PER'].to_list()
        # pbrList = df1['PBR'].to_list()
        # epsList = df1['EPS'].to_list()
        # closePrice = df2['종가'].to_list()
        #
        # print(perList)
        # print(pbrList)
        # print(epsList)
        # print(closePrice)

        x = df1[['PER', 'PBR', 'EPS']]
        y = df2[['종가']]

        x = x.to_numpy()
        y = y.to_numpy()

        df3 = stock.get_market_fundamental("2022-06-03", "2022-06-05", stockCode, freq='d', name_display=True)

        mlr = LinearRegression()
        mlr.fit(x, y)

        per_ = df3['PER'].values[0]
        pbr_ = df3['PBR'].values[0]
        eps_ = df3['EPS'].values[0]

        my_stock = [[per_, pbr_, eps_]]
        predict = mlr.predict(my_stock)
        print(predict)

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
            result.append(PyKRX(str(dateIndex[i])[0:10],
                                round(perList[i] * epsList[i], 2),
                                bpsList[i],
                                perList[i],
                                round(pbrList[i], 2),
                                epsList[i],
                                round(divList[i], 2),
                                dpsList[i]))

        return result

    def getDataFrameByStock(self, stockCode):
        # StartDate , EndDate, StockCode
        startDate = '20220101'
        endDate = '20220602'
        df = stock.get_market_fundamental(startDate, endDate, stockCode, freq='d', name_display=True)
        print(df)
        return df


if __name__ == '__main__':
    impl = PyKRXServiceImpl()
    impl.predict("039290")
