from pykrx import stock

if __name__ == '__main__':
    # StartDate , EndDate, StockCode
    startDate = '20220101'
    endDate = '20220522'
    stockCode = '005930'
    df = stock.get_market_fundamental(startDate, endDate, stockCode, freq='d', name_display=True)
    values = df.columns.values
    perList = df['PER'].tolist()
    pbrList = df['PBR'].tolist()

    ticker_list = stock.get_market_ticker_list()

    stockName: str

    print(stock.get_market_ticker_name(stockCode))
    print(startDate + " 부터 " + endDate + " 까지 평균 PER :: " + round((sum(perList) / len(perList)), 2).__str__())

    print(startDate + " 부터 " + endDate + " 까지 평균 PBR :: " + round((sum(pbrList) / len(pbrList)), 2).__str__(),
          end="\n\n")

    print(endDate + " PER :: " + str(round(perList[-1], 2)))
    print(endDate + " PBR :: " + str(round(pbrList[-1], 2)), end="\n\n")

    print(df)
