import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

start = datetime.datetime(2017, 1, 2)
end = datetime.datetime(2022, 6, 1)


def makeStockChart(code, sDay=start, eDay=end):
    datas = web.DataReader(code, 'yahoo', sDay, eDay)

    tmp = datas['Adj Close']
    datas['5MA'] = tmp.rolling(window=5).mean()
    datas['20MA'] = tmp.rolling(window=20).mean()
    datas['60MA'] = tmp.rolling(window=60).mean()
    datas['120MA'] = tmp.rolling(window=120).mean()

    plt.figure(figsize=(12, 6))

    plt.plot(datas.Close, label='Close')

    plt.plot(datas['5MA'], label='5MA')
    plt.plot(datas['20MA'], label='20MA')
    plt.plot(datas['60MA'], label='60MA')
    plt.plot(datas['120MA'], label='120MA')
    plt.title(code + "'s stock chart")
    plt.legend()
    plt.show()


def makeDataFrame(code, sDay=start, eDay=end):
    datas = web.DataReader(code, 'yahoo', sDay, eDay)

    df1 = pd.DataFrame(datas)
    print(df1.tail(5))

    dic = {
        'ds': datas.index,
        'y': datas.Close
    }

    df = pd.DataFrame(dic)

    df.reset_index(inplace=True)

    del df['Date']

    print(df.head(5))
    return df


if __name__ == '__main__':
    samsung_code = '005930.KS'
    data_df = makeDataFrame(samsung_code)

