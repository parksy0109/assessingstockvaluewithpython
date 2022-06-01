import abc


class StockService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getDatasByStockDTO(self, groupCode):
        # 주식 코드로 주식 이름 찾는 메소드
        raise NotImplemented
