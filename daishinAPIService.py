import win32com.client
import utilitys
import pandas as pd

# pands 설정
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)

# 대신 증권 API 오브젝트 가져오기
instCpCybos = win32com.client.Dispatch('CpUtil.CpCybos')
instCpStockCode = win32com.client.Dispatch('CpUtil.CpStockCode')
instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")
instCpCodMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")

# 데이터 담는 배열
stockcodes = []
stocknames = []
stockfullcodes = []
stockcurrentprice = []
stockper = []
stockeps = []
resonablestockprice = []
evaluatingbyper = []


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

    peraverage = sum(stockper) / len(stockper)
    printdataframe(peraverage)
    print()
    print(instCpCodMgr.GetIndustryName(groupcode) + " 해당 업종의 평균 PER = " + (sum(stockper) / len(stockper)).__str__())


def getindustrylist():
    industry_list = instCpCodMgr.GetIndustryList()
    for industry in industry_list:
        print(instCpCodMgr.GetIndustryName(industry) + " " + industry)


def convertcodetoname(code):
    name = instCpCodMgr.CodeToName(code)
    return name


def printdataframe(peraverage):
    for i in range(0, len(stockeps)):
        resonablestockprice.append(peraverage * stockeps[i])

    for per in stockper:
        if per < peraverage:
            evaluatingbyper.append("저평가")
        elif per == peraverage:
            evaluatingbyper.append("평균")
        elif per > peraverage:
            evaluatingbyper.append("고평가")

    data = {
        # '코드': stockcodes,
        '이름': stocknames,
        # '풀코드': stockfullcodes,
        '현재가': stockcurrentprice,
        'PER': stockper,
        'EPS': stockeps,
        '적정주가': resonablestockprice,
        '평가': evaluatingbyper
    }
    frame = pd.DataFrame(data)
    print(frame)
