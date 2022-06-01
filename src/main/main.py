from src.main.constants.GroupCodes import GroupCodes
from src.main.stock.StockServiceImpl import StockServiceImpl
from src.main.view.MainView import MainView
import win32com.client
from tkinter import messagebox


def checkConnecting():
    inCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
    if inCpCybos.IsConnect == 1:
        return True  # 정상 연결
    else:
        return False  # 연결 끊김

    # Press the green button in the gutter to run the script.


if __name__ == '__main__':
    impl = StockServiceImpl()
    view = MainView()

    groupName = "전기,전자"
    if checkConnecting():
        per_average = impl.getDatasByStockDTO(GroupCodes.GROUP_CODES[groupName])
        view.showTkinterTable(per_average, groupName)
    else:
        messagebox.showinfo("에러 메시지", "연결 끊긴 상태입니다. 연결을 확인 후 재 시도 해주세요.")
