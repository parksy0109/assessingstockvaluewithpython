import tkinter
import tkinter.ttk
from src.main.stock.StockService import StockService
from src.main.stock.StockServiceImpl import StockServiceImpl


class MainView:
    stockService: StockService = StockServiceImpl()

    def showTkinterTable(self):
        tk = tkinter.Tk()
        tk.title("")
