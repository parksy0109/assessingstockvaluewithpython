from src.main.constants.GroupCodes import GroupCodes
from src.main.stock.StockServiceImpl import StockServiceImpl
from src.main.view.MainView import MainView

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    impl = StockServiceImpl()
    view = MainView()

    per_average = impl.getRatedStocksAtPERAverage(GroupCodes.MACHINE)
    view.showTkinterTable(per_average)
