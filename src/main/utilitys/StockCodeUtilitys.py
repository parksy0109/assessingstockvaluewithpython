class StockCodeUtilitys:
    @staticmethod
    def makeFullCodeString(stockCode):
        stockCodeString = str(stockCode)

        stringLength = len(stockCodeString)

        if stringLength == 3:
            return "000" + stockCodeString
        elif stringLength == 4:
            return "00" + stockCodeString
        elif stringLength == 5:
            return "0" + stockCodeString
