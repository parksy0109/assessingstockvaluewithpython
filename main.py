# This is a sample Python script.
import daishinAPIService

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if daishinAPIService.checkconnecting() == 1:
        print("connecting complete")

    print(daishinAPIService.getdata(2,0))
    print(daishinAPIService.findbystockname("NAVER"))