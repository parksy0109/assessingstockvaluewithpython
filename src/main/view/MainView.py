import tkinter
from tkinter import *
from tkinter import ttk

from src.main.krx.PyKRXServiceImpl import PyKRXServiceImpl
from src.main.utilitys.StockCodeUtilitys import StockCodeUtilitys

from src.main.utilitys.LogUtils import Log
from src.main.krx.PyKRX import PyKRX

import matplotlib.pyplot as plt


class MainView:
    # GUI창을 생성하고 라벨을 설정한다.
    root = Tk()
    root.title("주식 가치 평가 Team 4")
    root.geometry("1600x700")
    root.resizable(False, False)

    # 트리뷰 초기화
    treeview = ttk.Treeview(root, columns=["one", "two", "three", "four", "five", "six", "seven"],
                            displaycolumns=["one", "two", "three", "four", "five", "six", "seven"], height=30)

    def showTkinterTable(self, list, grounName):

        stockPER: list[float] = []
        stockEPS: list[float] = []
        stockROE: list[float] = []

        for item in list:
            stockPER.append(item.priceEarningsRatio)
            stockEPS.append(item.earningPerShare)
            stockROE.append(item.returnOnEquity)

        averagePER = round(sum(stockPER) / len(stockPER), 2)
        averageEPS = round(sum(stockEPS) / len(stockEPS), 2)
        averageROE = round(sum(stockROE) / len(stockROE), 2)

        lbl = Label(self.root, text="업종 평균 PER 로 적정주가 계산")
        lbl.pack()

        lbl2 = Label(self.root,
                     text="업종 :: " + grounName + " 평균 PER :: " + averagePER.__str__() + " 평균 EPS :: " + averageEPS.__str__() + " 평균 ROE :: " + averageROE.__str__())
        lbl2.pack()

        # ﻿표 생성하기. colums는 컬럼 이름, displaycolums는 실행될 때 보여지는 순서다.
        # , "six", "seven"

        self.treeview.pack()

        # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
        self.treeview.column("#0", width=100, )
        self.treeview.heading("#0", text="순번")

        self.treeview.column("#1", width=200, anchor="center")
        self.treeview.heading("one", text="이름", anchor="center")

        self.treeview.column("#2", width=150, anchor="center")
        self.treeview.heading("two", text="코드", anchor="center")

        self.treeview.column("#3", width=200, anchor="center")
        self.treeview.heading("three", text="현재가", anchor="center")

        self.treeview.column("#4", width=150, anchor="center")
        self.treeview.heading("four", text="PER", anchor="center")

        self.treeview.column("#5", width=200, anchor="center")
        self.treeview.heading("five", text="EPS", anchor="center")

        self.treeview.column("#6", width=200, anchor="center")
        self.treeview.heading("six", text="ROE", anchor="center")

        self.treeview.column("#7", width=300, anchor="center")
        self.treeview.heading("seven", text="업종 평균 PER로 계산 한 적정주가", anchor="center")
        #
        # treeview.column("#7", width=200, anchor="center")
        # treeview.heading("seven", text="평가", anchor="center")

        for i in range(len(list)):
            value = [list[i].name, list[i].code, list[i].currentPrice, list[i].priceEarningsRatio,
                     list[i].earningPerShare,
                     list[i].returnOnEquity, list[i].reasonableStockPrice]
            # , list[i].reasonableStockPrice, list[i].evaluation
            self.treeview.insert('', 'end', text=i, values=value, iid=str(i) + "번")

        self.treeview.bind("<Double-1>", self.clickItem)
        # GUI 실행
        self.root.mainloop()

    def clickItem(self, event):
        selectedItem = self.treeview.focus()
        getValue = self.treeview.item(selectedItem).get('values')

        stringStockCode = StockCodeUtilitys.makeFullCodeString(getValue[1])

        impl = PyKRXServiceImpl()

        period = impl.getStockDataByPeriod(stringStockCode)

        Log.d("MainView", "clickItem", str(period[1].date))

        # GUI창을 생성하고 라벨을 설정한다.
        root2 = Tk()
        root2.title("상세 내용")
        root2.geometry("1600x700")
        root2.resizable(False, False)

        # 트리뷰 초기화
        treeview2 = ttk.Treeview(root2, columns=["one", "two", "three", "four", "five", "six", "seven"],
                                 displaycolumns=["one", "two", "three", "four", "five", "six", "seven"], height=30)

        labelTitle = Label(root2, text="해당 종목 상세 내역")
        labelTitle.pack()

        labelSubtiltle = Label(root2, text="오늘 날짜 데이터")
        labelSubtiltle.pack()

        labelContent = Label(root2, text=getValue)
        labelContent.pack()

        treeview2.pack()

        # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
        treeview2.column("#0", width=100, )
        treeview2.heading("#0", text="순번")

        treeview2.column("#1", width=200, anchor="center")
        treeview2.heading("one", text="날짜", anchor="center")

        treeview2.column("#2", width=150, anchor="center")
        treeview2.heading("two", text="주당순자산(BPS)", anchor="center")

        treeview2.column("#3", width=200, anchor="center")
        treeview2.heading("three", text="주가수익비율(PER)", anchor="center")

        treeview2.column("#4", width=150, anchor="center")
        treeview2.heading("four", text="주가순자산비율(PBR)", anchor="center")

        treeview2.column("#5", width=200, anchor="center")
        treeview2.heading("five", text="주당순이익(EPS)", anchor="center")

        treeview2.column("#6", width=200, anchor="center")
        treeview2.heading("six", text="배당수익률(DIV)", anchor="center")

        treeview2.column("#7", width=300, anchor="center")
        treeview2.heading("seven", text="주당배당금(DPS)", anchor="center")
        #
        # treeview.column("#7", width=200, anchor="center")
        # treeview.heading("seven", text="평가", anchor="center")

        for i in range(len(period)):
            value = [period[i].date, period[i].BPS, period[i].PER, period[i].PBR,
                     period[i].EPS,
                     period[i].DIV, period[i].DPS]
            treeview2.insert('', 'end', text=i, values=value, iid=str(i) + "번")

        root2.mainloop()

    def showGraph(self, PyKRXs):

        kr_xs = list[PyKRX](PyKRXs)

        x_date_list = []

        y1_BPS_list = []
        y2_PER_list = []
        y3_PBR_list = []
        y4_EPS_list = []
        y5_DIV_list = []
        y6_DPS_list = []

        for krx in kr_xs:
            # 그래프 x 축 값
            x_date_list.append(krx.date)

            # 그래프 y 축 값
            y1_BPS_list.append(krx.BPS)
            y2_PER_list.append(krx.PER)
            y3_PBR_list.append(krx.PBR)
            y4_EPS_list.append(krx.EPS)
            y5_DIV_list.append(krx.DIV)
            y6_DPS_list.append(krx.DPS)

        plt.plot(x_date_list, y1_BPS_list)  # 첫번째 라인 BPS
        plt.plot(x_date_list, y2_PER_list)  # 두번째 라인 PER
        plt.plot(x_date_list, y3_PBR_list)  # 세번째 라인 PBR
        plt.plot(x_date_list, y4_EPS_list)  # 네번째 라인 EPS
        plt.plot(x_date_list, y5_DIV_list)  # 다섯번째 라인 DIV
        plt.plot(x_date_list, y6_DPS_list)  # 여섯번째 라인 DPS
        plt.legend()
        plt.show()


if __name__ == '__main__':
    view = MainView()
