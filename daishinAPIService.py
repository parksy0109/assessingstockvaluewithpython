import win32com.client
import utilitys


# 연결 확인하는 함수 return 값 1일 경우 연결된 상태
def checkconnecting():
    instCpCybos = win32com.client.Dispatch('CpUtil.CpCybos')
    return instCpCybos.IsConnect


# 해당 인덱스의 종목 데이터를 반환
def getdata(type, index):
    utilitys.printlog("getdata", "type = " + type.__str__ + " index = " + index.__str__)
    instCpStockCode = win32com.client.Dispatch('CpUtil.CpStockCode')
    return instCpStockCode.GetData(type, index)


# 주식 이름으로 해당 인덱스랑 종목 코드 검색하는 함수
def findbystockname(stockname):
    utilitys.printlog("findbystockname", stockname)
    instCpStockCode = win32com.client.Dispatch('CpUtil.CpStockCode')
    stock_count = instCpStockCode.GetCount()
    for i in range(0, stock_count):
        if instCpStockCode.GetData(1, i) == stockname:
            return 'index = ' + i.__str__() + ' 종목 코드 = ' + instCpStockCode.GetData(0, i)


def getdatas():
    instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")  # 객체생성
    instMarketEye.SetInputValue(0, (4, 67, 70, 111))  # SetInputValue
    instMarketEye.SetInputValue(1, 'A005930')
    instMarketEye.BlockRequest()
    print("현재가: ", instMarketEye.GetDataValue(0, 0))  # GetData
    print("PER: ", instMarketEye.GetDataValue(1, 0))
    print("EPS: ", instMarketEye.GetDataValue(2, 0))
    print("최근분기년월: ", instMarketEye.GetDataValue(3, 0))


def getgroupcodelist(groupcode):
    instCpCodMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    cod_list = instCpCodMgr.GetGroupCodeList(groupcode)
    for code in cod_list:
        print(convertcodetoname(code))


def getindustrylist():
    instCpCodMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    industry_list = instCpCodMgr.GetIndustryList()
    for industry in industry_list:
        print(instCpCodMgr.GetIndustryName(industry) + " " + industry)


def convertcodetoname(code):
    instCpCodMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    name = instCpCodMgr.CodeToName(code)
    return name
