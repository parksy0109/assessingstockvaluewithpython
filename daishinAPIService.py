import win32com.client


# 연결 확인하는 함수 return 값 1일 경우 연결된 상태
def checkconnecting():
    instCpCybos = win32com.client.Dispatch('CpUtil.CpCybos')
    return instCpCybos.IsConnect


# 해당 인덱스의 종목 데이터를 반환
def getdata(type, index):
    instCpStockCode = win32com.client.Dispatch('CpUtil.CpStockCode')
    return instCpStockCode.GetData(type, index)


# 주식 이름으로 해당 인덱스랑 종목 코드 검색하는 함수
def findbystockname(stockname):
    instCpStockCode = win32com.client.Dispatch('CpUtil.CpStockCode')
    stock_count = instCpStockCode.GetCount()
    for i in range(0, stock_count):
        if instCpStockCode.GetData(1, i) == 'NAVER':
            return 'index = ' + i.__str__() + ' 종목 코드 = ' + instCpStockCode.GetData(0, i)
