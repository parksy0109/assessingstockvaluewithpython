from tkinter import *
from tkinter import ttk
from src.main.stock.StockService import StockService
from src.main.stock.StockServiceImpl import StockServiceImpl
from src.main.dto.StockValuationDTO import StockValuationDTO


class MainView:
    stockService: StockService = StockServiceImpl()

    def showTkinterTable(self, list):
        # GUI창을 생성하고 라벨을 설정한다.
        root = Tk()
        root.title("주식 가치 평가 Team 4")
        root.geometry("1600x700")
        root.resizable(False, False)

        lbl = Label(root, text="업종 평균 PER 로 적정주가 계산")
        lbl.pack()

        # ﻿표 생성하기. colums는 컬럼 이름, displaycolums는 실행될 때 보여지는 순서다.
        treeview = ttk.Treeview(root, columns=["one", "two", "three", "four", "five", "six"],
                                displaycolumns=["one", "two", "three", "four", "five", "six"], height=30)
        treeview.pack()

        # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
        treeview.column("#0", width=100, )
        treeview.heading("#0", text="순번")

        treeview.column("#1", width=100, anchor="center")
        treeview.heading("one", text="이름", anchor="center")

        treeview.column("#2", width=200, anchor="center")
        treeview.heading("two", text="현재가", anchor="center")

        treeview.column("#3", width=200, anchor="center")
        treeview.heading("three", text="PER", anchor="center")

        treeview.column("#4", width=200, anchor="center")
        treeview.heading("four", text="EPS", anchor="center")

        treeview.column("#5", width=200, anchor="center")
        treeview.heading("five", text="적정주가", anchor="center")

        treeview.column("#6", width=200, anchor="center")
        treeview.heading("six", text="평가", anchor="center")

        for i in range(len(list)):
            value = [list[i].name, list[i].currentPrice, list[i].priceEarningsRatio, list[i].earningPerShare,
                     list[i].reasonableStockPrice, list[i].evaluation]
            treeview.insert('', 'end', text=i, values=value, iid=str(i) + "번")

        # GUI 실행
        root.mainloop()


if __name__ == '__main__':
    view = MainView()
    view.showTkinterTable('d')
