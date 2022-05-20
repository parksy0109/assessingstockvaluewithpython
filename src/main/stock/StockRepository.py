import abc


class StockRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def findStockCodeByStockName(self, stockName):
        raise NotImplemented

    @abc.abstractmethod
    def findByStockCode(self, stockCode):
        raise NotImplemented

    @abc.abstractmethod
    def findStockCodesByGroupCode(self, groupCode):
        raise NotImplemented

    @abc.abstractmethod
    def findStocksByGroupCode(self, groupCode):
        raise NotImplemented
