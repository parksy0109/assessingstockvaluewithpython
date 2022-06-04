import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

if __name__ == '__main__':
    start = datetime.datetime(2017, 1, 2)
    end = datetime.datetime(2022, 6, 1)

    Df = web.DataReader('005930.KS', 'yahoo', start, end)
    Df = Df[['Close']]

    Df = Df.dropna()
    Df.Close.plot(figsize=(10, 5))
    plt.ylabel("Samsung Stock Price")

    Df['S_3'] = Df['Close'].shift(1).rolling(window=3).mean()
    Df['S_9'] = Df['Close'].shift(1).rolling(window=9).mean()
    Df = Df.dropna()
    X = Df[['S_3', 'S_9']]
    X.head()
    y = Df['Close']
    y.head()

    t = .8
    t = int(t * len(Df))
    # Train dataset
    X_train = X[:t]
    y_train = y[:t]
    # Test dataset
    X_test = X[t:]
    y_test = y[t:]

    linear = LinearRegression().fit(X_train, y_train)

    r2_score = linear.score(X[t:], y[t:]) * 100
    print(float("{0:.2f}".format(r2_score)))

    predicted_price = linear.predict(X_test)
    predicted_price = pd.DataFrame(predicted_price, index=y_test.index, columns=['price'])
    predicted_price.plot(figsize=(10, 5))
    y_test.plot()
    plt.legend(['predicted_price', 'actual_price'])
    plt.ylabel("Samsung Price")
    plt.show()


