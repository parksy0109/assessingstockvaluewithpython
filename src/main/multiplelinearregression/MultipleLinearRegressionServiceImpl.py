from pykrx import stock

from src.main.krx.PyKRXServiceImpl import PyKRXServiceImpl
from src.main.multiplelinearregression.MultipleLinearRegressionService import MultipleLinearRegressionService

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


class MultipleLinearRegressionServiceImpl(MultipleLinearRegressionService):
    def forecastingStockPriceByMultiLinearRegression(self, stockCode):
        impl = PyKRXServiceImpl()
        df = impl.getDataFrameByStock(stockCode)

        X = df.drop(columns=['PER'])
        Y = df['PER']

        x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.8, test_size=0.2)

        regression = LinearRegression()
        regression.fit(x_train, y_train)

        beta_0 = regression.intercept_  # PER
        beta_1 = regression.coef_[0]
        beta_2 = regression.coef_[1]
        beta_3 = regression.coef_[2]
        beta_4 = regression.coef_[3]
        beta_5 = regression.coef_[4]

        print("%f" % beta_0)
        print("%f" % beta_1)
        print("%f" % beta_2)
        print("%f" % beta_3)
        print("%f" % beta_4)
        print("%f" % beta_5)
        pass


if __name__ == '__main__':
    impl = MultipleLinearRegressionServiceImpl()
    impl.forecastingStockPriceByMultiLinearRegression("005930")
