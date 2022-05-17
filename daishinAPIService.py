import win32com.client
import utilitys
import pandas as pd

instCpCybos = win32com.client.Dispatch('CpUtil.CpCybos')
instCpStockCode = win32com.client.Dispatch('CpUtil.CpStockCode')
instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")
instCpCodMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")

stockcodes = []
stocknames = []
stockfullcodes = []
stockcurrentprice = []
stockper = []
stockeps = []


# 연결 확인하는 함수 return 값 1일 경우 연결된 상태
def checkconnecting():
    print(instCpCybos.IsConnect)
    if instCpCybos.IsConnect == 1:
        print("연결 정상")
    else:
        print("연결 끊김")


# 해당 인덱스의 종목 데이터를 반환 0 - 종목코드, 1 - 종목명, 2 - FullCode
def getdata(code):
    stockcodes.append(instCpStockCode.GetData(0, instCpStockCode.CodeToIndex(code)))
    stocknames.append(instCpStockCode.GetData(1, instCpStockCode.CodeToIndex(code)))
    stockfullcodes.append(instCpStockCode.GetData(2, instCpStockCode.CodeToIndex(code)))
    getdatas(code)


# 주식 이름으로 해당 인덱스랑 종목 코드 검색하는 함수
def findbystockname(stockname):
    utilitys.printlog("findbystockname", stockname)
    stock_count = instCpStockCode.GetCount()
    for i in range(0, stock_count):
        if instCpStockCode.GetData(1, i) == stockname:
            return 'index = ' + i.__str__() + ' 종목 코드 = ' + instCpStockCode.GetData(0, i)


def getdatas(stockcode):
    instMarketEye.SetInputValue(0, (4, 67, 70, 111))  # SetInputValue
    instMarketEye.SetInputValue(1, stockcode)
    instMarketEye.BlockRequest()
    stockcurrentprice.append(instMarketEye.GetDataValue(0, 0))
    stockper.append(instMarketEye.GetDataValue(1, 0))
    stockeps.append(instMarketEye.GetDataValue(2, 0))
    # print("최근분기년월: ", instMarketEye.GetDataValue(3, 0))


def getgroupcodelist(groupcode):
    cod_list = instCpCodMgr.GetGroupCodeList(groupcode)
    for code in cod_list:
        getdata(code)

    printdataframe()


def getindustrylist():
    industry_list = instCpCodMgr.GetIndustryList()
    for industry in industry_list:
        print(instCpCodMgr.GetIndustryName(industry) + " " + industry)


def convertcodetoname(code):
    name = instCpCodMgr.CodeToName(code)
    return name


def printdataframe():
    data = {
        '0': stockcodes,
        '1': stocknames,
        '2': stockfullcodes,
        '3': stockcurrentprice,
        '4': stockper,
        '5': stockeps,
    }
    frame = pd.DataFrame(data)
    print(frame)
