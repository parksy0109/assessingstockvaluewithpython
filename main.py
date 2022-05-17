# This is a sample Python script.
import constants
import daishinAPIService

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if daishinAPIService.checkconnecting() == 1:
        print("connecting complete")

    daishinAPIService.getgroupcodelist(constants.chemistry)