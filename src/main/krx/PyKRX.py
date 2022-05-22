from pykrx import stock

if __name__ == '__main__':
    # StartDate , EndDate, StockCode
    startDate = '20220101'
    endDate = '20220522'
    stockCode = '005930'
    df = stock.get_market_fundamental(startDate, endDate, stockCode)
    print(df)
