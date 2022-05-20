import sys


class Log:
    @staticmethod
    def d(className, functionName, parameter):
        # 디버그 상황에서만 로그 찍히게
        attr = getattr(sys, 'gettrace', None)

        if attr is None:
            return
        elif attr():
            print(className + "." + functionName + " :: " + parameter)
        else:
            return
