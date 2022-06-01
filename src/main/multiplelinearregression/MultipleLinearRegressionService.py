import abc


class MultipleLinearRegressionService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def forecastingStockPriceByMultiLinearRegression(self, groupCode):
        raise NotImplemented
