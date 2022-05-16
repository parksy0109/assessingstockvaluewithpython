import constants
import requests
from bs4 import BeautifulSoup
import pandas as pd

# pands 설정
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)

# 종목 이름 담는 배열
stockNames = []

# 종목 현재가 담는 배열
stockCurrentPrices = []

# 종목 전일비 담는 배열
stockPreviousDaysExpenses = []

# 종목 등락률 담는 배열
stockRateOfFluctuations = []

# 종목 매수호가 거래량 거래대금 전일거래량
stockBuyingPrices = []

# 종목 매도호가
stockSellingPrice = []

# 종목 거래량
stockVolumes = []

# 종목 거래대금
stockTransactionPrices = []

# 전일 거래량
stockVolumesOfTransactionsOnPreviousDay = []


def crawling(code):
    url = 'https://finance.naver.com/sise/sise_group_detail.naver?type=upjong&no=' + code

    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        stock_number = soup.findAll("td", {"class": "number"})
        stock_name = soup.findAll("div", {"class": "name_area"})
        for idx in range(len(stock_name)):
            stockNames.append(stock_name[idx].text.strip('*')[0:2])
            stockCurrentPrices.append(stock_number[8 * idx + 5].text.strip())
            stockPreviousDaysExpenses.append(stock_number[8 * idx + 6].text.strip())
            stockRateOfFluctuations.append(stock_number[8 * idx + 7].text.strip())
            stockBuyingPrices.append(stock_number[8 * idx + 8].text.strip())
            stockSellingPrice.append(stock_number[8 * idx + 9].text.strip())
            stockVolumes.append(stock_number[8 * idx + 10].text.strip())
            stockTransactionPrices.append(stock_number[8 * idx + 11].text.strip())
            stockVolumesOfTransactionsOnPreviousDay.append(stock_number[8 * idx + 12].text.strip())


    else:
        print(response.status_code)

    dataframe = pd.DataFrame(
        {
            'A': pd.Categorical(stockNames),  # 종목명
            'B': pd.Categorical(stockCurrentPrices),  # 현재가
            'C': stockPreviousDaysExpenses,  # 전일비
            'D': stockRateOfFluctuations,  # 등락률
            'E': stockBuyingPrices,  # 매수호가
            'F': stockSellingPrice,  # 매도호가
            'G': stockVolumes,  # 거래량
            'H': stockTransactionPrices,  # 거래대금
            'I': stockVolumesOfTransactionsOnPreviousDay  # 전일거래량
        }
    )
    # print(tabulate(dataframe, headers='keys', tablefmt='psql'))
    print(dataframe)


if __name__ == "__main__":
    crawling(constants.semiconductor_code)
