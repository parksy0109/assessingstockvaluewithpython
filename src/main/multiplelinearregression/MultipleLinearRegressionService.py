import abc


class MultipleLinearRegressionService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getRatedStocksAtPERAverage(self, groupCode):
        raise NotImplemented
