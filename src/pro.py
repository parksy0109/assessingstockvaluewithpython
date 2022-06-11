from src.main.constants.GroupCodes import GroupCodes
from src.main.stock.StockServiceImpl import StockServiceImpl
from src.main.view.MainView import MainView
import win32com.client
from tkinter import messagebox
from tkinter import *
from src.main.krx.PyKRXServiceImpl import PyKRXServiceImpl

if __name__ == '__main__':
    impl = StockServiceImpl()
    per_average = impl.getDatasByStockDTO("005")
    stockCodeList: list[str] = []

    for i in per_average:
        stockCodeList.append(i.code)

    impl2 = PyKRXServiceImpl()
    impl2.predictlist(stockCodeList)
